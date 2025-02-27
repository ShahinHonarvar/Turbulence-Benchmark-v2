def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(t):
    x = t[30]
    right_truncatable_primes = []
    for num in range(2, x):
        if is_prime(num):
            temp = num
            while temp > 0:
                if not is_prime(temp):
                    break
                temp //= 10
            if temp == 0:
                right_truncatable_primes.append(num)
    return sorted(right_truncatable_primes, reverse=True)