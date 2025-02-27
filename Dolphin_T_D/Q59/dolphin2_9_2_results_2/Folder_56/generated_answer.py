def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(x):
    x = x[30]
    primes = []
    for num in range(2, x):
        left = num
        left_list = []
        while left > 0:
            if is_prime(left):
                left_list.append(left)
            left //= 10
        if len(left_list) == len(str(num)):
            primes.append(num)
    return sorted(primes)