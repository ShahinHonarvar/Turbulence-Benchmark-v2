def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(num_tuple):
    x = num_tuple[50]
    left_truncatable_primes = []
    for num in range(x - 1, 1, -1):
        if '0' in str(num):
            continue
        n = num
        while n > 0 and is_prime(n):
            n //= 10
        if n > 0:
            continue
        temp = num
        while temp > 0:
            if not is_prime(temp):
                break
            temp //= 10
        if temp == 0:
            left_truncatable_primes.append(num)
    return left_truncatable_primes