def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def left_truncatable_primes(n):
    result = []
    for i in range(1, n):
        num = i
        while num > 0:
            if not is_prime(num):
                break
            num = num // 10
        if num == 0:
            result.append(i)
    return result

def all_left_truncatable_prime(x):
    return sorted(left_truncatable_primes(x))