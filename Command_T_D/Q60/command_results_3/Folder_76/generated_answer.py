import itertools

def all_left_right_truncatable_prime(n):
    if not n:
        return []

    def is_left_right_truncatable(x):
        if not x:
            return True
        if 0 in str(x):
            return False
        if not str(x)[0] and (not str(x)[-1]):
            return True
        if str(x)[0] == '0' and str(x)[-1] == '0':
            return True
        if str(x)[0] == '0':
            return False
        if str(x)[-1] == '0':
            return False
        return True

    def get_left_right_truncatable_primes(x):
        left_right_truncatable_primes = []
        primes = []
        indices = []
        if x[0] < 2:
            return left_right_truncatable_primes
        first_prime = next(x[1:], None)
        if is_left_right_truncatable(first_prime):
            left_right_truncatable_primes.append(first_prime)
            primes.append(first_prime)
            indices.append(0)
        for i in range(1, len(x)):
            if x[i] > 1:
                if is_left_right_truncatable(x[i]):
                    left_right_truncatable_primes.append(x[i])
                    primes.append(x[i])
                    indices.append(i)
        last_prime = next(x[:-1], None)
        if is_left_right_truncatable(last_prime):
            left_right_truncatable_primes.append(last_prime)
            primes.append(last_prime)
            indices.append(len(x) - 1)
        indices.sort()
        left_right_truncatable_primes = [primes[i] for i in indices]
        left_right_truncatable_primes.sort()
        return left_right_truncatable_primes
    return get_left_right_truncatable_primes(n)