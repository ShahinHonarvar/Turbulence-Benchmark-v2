def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def right_truncate(num):
    return num // 10

def all_right_truncatable_prime(numbers):
    primes = []
    for num in numbers:
        while num > 9:
            if not is_prime(num):
                break
            num = right_truncate(num)
        if is_prime(num) and num < numbers[177]:
            primes.append(num)
    return sorted(primes)