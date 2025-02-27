def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def all_left_right_truncatable_prime(v):
    x = v[175]
    primes = []
    for num in range(2, x + 1):
        if '0' not in str(num) and is_prime(num):
            temp = num
            while temp > 9:
                if not is_prime(temp):
                    break
                temp //= 10
            if temp <= 1:
                primes.append(num)
    primes.sort()
    return primes