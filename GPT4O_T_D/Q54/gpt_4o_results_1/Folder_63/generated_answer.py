def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(numbers):
    if len(numbers) <= 88:
        return []
    x = numbers[88]
    if x < 2:
        return []
    primes = []
    for num in range(2, x):
        str_num = str(num)
        truncatable = True
        while len(str_num) > 0:
            if not is_prime(int(str_num)):
                truncatable = False
                break
            str_num = str_num[:-1]
        if truncatable:
            primes.append(num)
    return sorted(primes)