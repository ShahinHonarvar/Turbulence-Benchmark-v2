def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(t):
    x = t[55]
    right_truncatable_primes = []
    for num in range(x, 1, -1):
        if is_prime(num):
            trunc = num
            while trunc > 1:
                if not is_prime(trunc):
                    break
                trunc //= 10
            else:
                right_truncatable_primes.append(num)
    return sorted(right_truncatable_primes, reverse=True)