def all_left_right_truncatable_prime(numbers):
    x = numbers[10]
    primes = []
    for num in range(x, 1, -1):
        if is_prime(num) and is_truncatable_prime(num):
            primes.append(num)
    return sorted(primes, reverse=True)

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def is_truncatable_prime(num):
    num_str = str(num)
    while len(num_str) > 1:
        if not is_prime(int(num_str)):
            return False
        num_str = num_str[1:]
        if not is_prime(int(num_str)):
            return False
        num_str = num_str[:-1]
    return is_prime(int(num_str))