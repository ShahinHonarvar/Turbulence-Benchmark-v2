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

def all_right_truncatable_prime(numbers):
    if not numbers or not all((i > 0 for i in numbers)):
        return []
    x = numbers[49]
    primes = []
    for num in range(2, x):
        if is_prime(num):
            truncate = num
            while truncate:
                if not is_prime(truncate):
                    break
                truncate //= 10
            else:
                primes.append(num)
    return sorted(primes)