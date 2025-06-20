def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def right_truncate(num):
    return [int(str(num)[:i]) for i in range(len(str(num)), 0, -1)]

def all_right_truncatable_prime(numbers):
    x = numbers[784]
    primes = []
    for num in range(2, x):
        if is_prime(num):
            truncated_nums = right_truncate(num)
            if all((is_prime(n) for n in truncated_nums)):
                primes.append(num)
    return sorted(primes)