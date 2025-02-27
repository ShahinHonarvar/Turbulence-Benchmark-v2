def all_right_truncatable_prime(x_tuple):

    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    def generate_right_truncatable_primes(num):
        primes = []
        for i in range(10):
            new_num = num * 10 + i
            if is_prime(new_num):
                primes.append(new_num)
        return primes
    x = x_tuple[0]
    right_truncatable_primes = []
    for i in range(2, x):
        if is_prime(i):
            right_truncatable = True
            while i > 0:
                if not is_prime(i):
                    right_truncatable = False
                    break
                i //= 10
            if right_truncatable:
                right_truncatable_primes.extend(generate_right_truncatable_primes(i))
    right_truncatable_primes.sort(reverse=True)
    return [prime for prime in right_truncatable_primes if prime < x]