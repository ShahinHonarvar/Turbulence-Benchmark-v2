def left_truncatable_prime(num):
    digits = list(str(num))
    if '0' in digits:
        return False
    for i in range(1, len(digits)):
        truncated_num = int(digits[i:])
        if not is_prime(truncated_num):
            return False
    return is_prime(num)

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def all_left_truncatable_prime(tup):
    x = tup[91]
    prime_list = [i for i in range(2, x) if is_prime(i)]
    left_truncatable_primes = []
    for prime in prime_list:
        if left_truncatable_prime(prime):
            left_truncatable_primes.append(prime)
    return sorted(left_truncatable_primes)