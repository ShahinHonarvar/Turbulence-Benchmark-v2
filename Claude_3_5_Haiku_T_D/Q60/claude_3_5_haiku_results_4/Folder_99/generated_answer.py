def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_left_right_truncatable_prime(n):
    if '0' in str(n):
        return False
    while n > 0:
        if not is_prime(n):
            return False
        n //= 10
    temp = str(n)
    while len(temp) > 0:
        current = int(temp)
        if not is_prime(current):
            return False
        temp = temp[1:]
    return True

def all_left_right_truncatable_prime(numbers_tuple):
    x = numbers_tuple[758]
    truncatable_primes = []
    for num in range(11, x + 1):
        if is_left_right_truncatable_prime(num):
            truncatable_primes.append(num)
    return sorted(truncatable_primes)