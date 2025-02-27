def is_prime(n):
    if n in (2, 3):
        return True
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(t):
    x = t[69]
    left_right_truncatable_primes = []
    for num in range(2, x + 1):
        if '0' not in str(num):
            n = num
            while n > 9:
                n = n // 10
                if not is_prime(n):
                    break
            else:
                n = num
                while n > 9:
                    n = n // 10
                    if not is_prime(n):
                        break
                else:
                    left_right_truncatable_primes.append(num)
    return sorted(left_right_truncatable_primes, reverse=True)