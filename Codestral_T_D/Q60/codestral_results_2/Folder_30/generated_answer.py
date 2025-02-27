def all_left_right_truncatable_prime(numbers):
    x = numbers[37]
    trunc_primes = []
    for num in range(2, x + 1):
        if is_prime(num) and is_left_truncatable(num) and is_right_truncatable(num):
            trunc_primes.append(num)
    return sorted(trunc_primes, reverse=True)

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def is_left_truncatable(num):
    num_str = str(num)
    for i in range(1, len(num_str)):
        if num_str[i] == '0':
            return False
        trunc_num = int(num_str[i:])
        if not is_prime(trunc_num):
            return False
    return True

def is_right_truncatable(num):
    num_str = str(num)
    for i in range(1, len(num_str)):
        if num_str[-i] == '0':
            return False
        trunc_num = int(num_str[:-i])
        if not is_prime(trunc_num):
            return False
    return True