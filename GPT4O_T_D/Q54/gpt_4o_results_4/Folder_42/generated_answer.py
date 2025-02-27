def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def right_truncatable_primes(x):
    primes = []
    stack = [2, 3, 5, 7]
    while stack:
        num = stack.pop()
        if num < x and is_prime(num):
            primes.append(num)
            for digit in range(10):
                new_num = num * 10 + digit
                if new_num < x:
                    stack.append(new_num)
    return primes

def all_right_truncatable_prime(numbers):
    if len(numbers) <= 64:
        return []
    x = numbers[64]
    result = right_truncatable_primes(x)
    return sorted(result, reverse=True)