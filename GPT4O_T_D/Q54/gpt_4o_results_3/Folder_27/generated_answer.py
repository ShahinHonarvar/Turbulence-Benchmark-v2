def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def generate_right_truncatable_primes(upper_limit):
    primes = []
    queue = [2, 3, 5, 7]
    while queue:
        num = queue.pop(0)
        if num < upper_limit:
            primes.append(num)
            for digit in range(10):
                candidate = num * 10 + digit
                if is_prime(candidate):
                    queue.append(candidate)
    return primes

def all_right_truncatable_prime(numbers):
    if len(numbers) <= 79:
        return []
    x = numbers[79]
    if type(x) is not int or x <= 0:
        return []
    result = generate_right_truncatable_primes(x)
    return sorted(result, reverse=True)