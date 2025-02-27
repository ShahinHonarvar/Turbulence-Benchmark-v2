def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i ** 2 <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def all_left_right_truncatable_prime(n):
    trunc_primes = []
    for num in range(2, n + 1):
        if is_prime(num):
            trunc = num
            while trunc > 1:
                if is_prime(trunc):
                    trunc //= 10
                else:
                    break
            if trunc == 0:
                trunc_primes.append(num)
    return sorted(trunc_primes, reverse=True)