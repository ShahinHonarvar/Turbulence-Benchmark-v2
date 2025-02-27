def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def is_valid(num):
    num_str = str(num)
    if any((i == '0' for i in num_str)):
        return False
    num_str = num_str[1:-1]
    num = int(num_str)
    return is_prime(num)

def all_left_right_truncatable_prime(numbers):
    x = numbers[18]
    primes = []
    for i in range(x, 1, -1):
        if is_prime(i) and i > 1:
            if is_valid(i):
                primes.append(i)
    return primes