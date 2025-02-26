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
    for length in range(len(str(n)), 0, -1):
        left_trunc = int(str(n)[0:length])
        right_trunc = int(str(n)[-length:])
        while length > 0:
            if not is_prime(left_trunc) or not is_prime(right_trunc):
                return False
            if length > 1:
                left_trunc //= 10
                right_trunc %= 10 ** (length - 1)
            length -= 1
    return True

def all_left_right_truncatable_prime(tup):
    x = tup[77]
    truncatable_primes = [num for num in range(2, x + 1) if is_prime(num) and is_left_right_truncatable_prime(num)]
    return sorted(truncatable_primes, reverse=True)