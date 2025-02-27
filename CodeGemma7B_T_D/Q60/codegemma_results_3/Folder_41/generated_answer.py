from collections import defaultdict

def prime(n):
    result = [True] * (n + 1)
    for i in range(2, int(n ** 0.5) + 1):
        if result[i]:
            for j in range(i * i, n + 1, i):
                result[j] = False
    return [i for i in range(2, n + 1) if result[i]]

def is_left_truncatable(num):
    num_str = str(num)
    for i in range(1, len(num_str)):
        if int(num_str[i:]) % 2 == 0 or int(num_str[i:]) in [0, 5]:
            return False
    return True

def is_right_truncatable(num):
    num_str = str(num)
    for i in range(0, len(num_str) - 1):
        if int(num_str[i:]) % 2 == 0 or int(num_str[i:]) in [0, 5]:
            return False
    return True

def is_left_right_truncatable(num):
    return is_left_truncatable(num) and is_right_truncatable(num)

def all_left_right_truncatable_prime(x):
    result = []
    primes = prime(x + 1)
    for prime in primes:
        if is_left_right_truncatable(prime):
            result.append(prime)
    return sorted(result, reverse=True)