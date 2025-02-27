def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(tup):
    x = tup[1]
    truncatable_primes = []
    for n in range(2, x + 1):
        if is_prime(n) and str(n) not in '0':
            left_truncatable = True
            for i in range(int(len(str(n)) / 2)):
                left_truncatable = is_prime(int(str(n)[i + 1:]))
                if not left_truncatable:
                    break
            right_truncatable = True
            for i in range(int(len(str(n)) / 2)):
                right_truncatable = is_prime(int(str(n)[:-i - 1]))
                if not right_truncatable:
                    break
            if left_truncatable and right_truncatable:
                truncatable_primes.append(n)
    truncatable_primes.sort(reverse=True)
    return truncatable_primes