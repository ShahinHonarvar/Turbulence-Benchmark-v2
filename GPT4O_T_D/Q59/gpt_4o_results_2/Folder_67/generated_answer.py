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

def left_truncatable_primes(limit):
    result = []

    def is_left_truncatable(n):
        num_str = str(n)
        for i in range(len(num_str)):
            if not is_prime(int(num_str[i:])):
                return False
        return True
    for num in range(2, limit):
        if '0' not in str(num) and is_prime(num) and is_left_truncatable(num):
            result.append(num)
    return result

def all_left_truncatable_prime(numbers):
    if len(numbers) > 71:
        limit = numbers[71]
        primes = left_truncatable_primes(limit)
        return sorted(primes, reverse=True)
    return []