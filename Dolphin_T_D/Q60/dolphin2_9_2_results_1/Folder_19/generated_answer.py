def all_left_right_truncatable_prime(num_tuple):
    x = num_tuple[67]
    left_right_truncatable_primes = []
    for i in range(2, x + 1):
        if is_prime(i) and i != 0 and is_truncatable(i):
            left_right_truncatable_primes.append(i)
    return sorted(left_right_truncatable_primes, reverse=True)

def is_prime(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

def is_truncatable(num):
    num_str = str(num)
    for i in range(len(num_str) - 1):
        if not is_prime(int(num_str[i + 1:])) or not is_prime(int(num_str[:i + 1])):
            return False
    return True