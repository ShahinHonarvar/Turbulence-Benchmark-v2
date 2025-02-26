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
        truncated = n
        while len(str(truncated)) > 1:
            truncated = int(str(truncated)[1:])
            if not is_prime(truncated):
                return False
        truncated = n
        while len(str(truncated)) > 1:
            truncated = int(str(truncated)[:-1])
            if not is_prime(truncated):
                return False
    return is_prime(n)

def all_left_right_truncatable_prime(input_tuple):
    x = input_tuple[52]
    truncatable_primes = []
    for num in range(x, 1, -1):
        if is_left_right_truncatable_prime(num):
            truncatable_primes.append(num)
    return truncatable_primes