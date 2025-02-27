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

def generate_truncatable_primes(limit):
    left_truncatable_primes = []
    queue = ['2', '3', '5', '7']
    while queue:
        candidate = queue.pop(0)
        num = int(candidate)
        if num < limit and is_prime(num):
            left_truncatable_primes.append(num)
            for digit in '1379':
                new_candidate = candidate + digit
                queue.append(new_candidate)
    return left_truncatable_primes

def all_left_truncatable_prime(numbers):
    x = numbers[39]
    truncatable_primes = generate_truncatable_primes(x)
    return sorted(truncatable_primes)