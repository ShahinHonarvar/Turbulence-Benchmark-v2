def is_prime(n):
    if n <= 1 or (n % 2 == 0 and n > 2) or (n > 5 and n % 5 == 0):
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def left_right_truncatable_prime(n):
    if str(n).count('0') > 0:
        return False
    for i in range(len(str(n))):
        if not is_prime(int(str(n)[:i]) if i < len(str(n)) - 1 else int(str(n)[:-1])) or not is_prime(int(str(n)[i + 1:]) if i < len(str(n)) - 1 else int(str(n)[:-1])):
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    truncatable_primes = []
    for num in numbers:
        if left_right_truncatable_prime(num):
            truncatable_primes.append(num)
    return sorted(truncatable_primes, reverse=True)