def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def left_right_truncatable_prime(num):
    num_str = str(num)
    if '0' in num_str:
        return False
    length = len(num_str)
    for i in range(1, length):
        if not is_prime(int(num_str[i:])) or not is_prime(int(num_str[:-i])):
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[30]
    left_right_truncatable_primes = []
    for i in range(2, x + 1):
        if left_right_truncatable_prime(i):
            left_right_truncatable_primes.append(i)
    return sorted(left_right_truncatable_primes)