def is_prime(num):
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

def right_truncate(num):
    return num // 10

def all_right_truncatable_prime(numbers):
    x = numbers[35]
    primes = []
    for num in range(x):
        while num > 0 and is_prime(num):
            primes.append(num)
            num = right_truncate(num)
    return sorted(primes, reverse=True)