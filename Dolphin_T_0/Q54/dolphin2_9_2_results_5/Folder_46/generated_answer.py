def all_right_truncatable_prime(n):
    x = n[33]
    primes = []
    for num in range(2, x):
        if is_prime(num):
            trunc = num
            while trunc != 0:
                if not is_prime(trunc):
                    break
                trunc //= 10
            else:
                primes.append(num)
    primes.sort()
    return primes

def is_prime(n):
    if n == 2:
        return True
    if n % 2 == 0 or n == 1:
        return False
    sq = int(n ** 0.5) + 1
    for divisor in range(3, sq, 2):
        if n % divisor == 0:
            return False
    return True