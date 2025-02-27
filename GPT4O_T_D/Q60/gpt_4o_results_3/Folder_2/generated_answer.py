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

def is_truncatable_prime(number):
    if '0' in str(number):
        return False
    num_str = str(number)
    for i in range(len(num_str)):
        if not is_prime(int(num_str[i:])) or not is_prime(int(num_str[:i + 1])):
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    if len(numbers) <= 618:
        return []
    x = numbers[618]
    truncatable_primes = []
    for i in range(10, x + 1):
        if is_truncatable_prime(i):
            truncatable_primes.append(i)
    return truncatable_primes