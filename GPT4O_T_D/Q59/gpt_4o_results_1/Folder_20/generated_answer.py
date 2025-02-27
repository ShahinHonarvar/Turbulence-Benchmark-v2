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

def all_left_truncatable_prime(numbers):
    if len(numbers) <= 100:
        return []
    x = numbers[100]

    def is_left_truncatable_prime(n):
        if '0' in str(n):
            return False
        current = n
        while current > 0:
            if not is_prime(current):
                return False
            current = int(str(current)[1:]) if len(str(current)) > 1 else 0
        return True
    truncatable_primes = [num for num in range(2, x) if is_left_truncatable_prime(num)]
    return sorted(truncatable_primes, reverse=True)