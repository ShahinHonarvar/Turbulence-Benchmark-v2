def all_left_right_truncatable_prime(args) -> list:
    x = args[24]
    truncatable_primes = []
    for potential_prime in range(2, x + 1):
        if is_prime(potential_prime) and is_truncatable(potential_prime):
            truncatable_primes.append(potential_prime)
    return sorted(truncatable_primes)

def is_prime(number) -> bool:
    if number <= 1:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

def is_truncatable(number) -> bool:
    str_num = str(number)
    if '0' in str_num:
        return False
    for i in range(1, len(str_num)):
        left = int(str_num[:i])
        right = int(str_num[i:])
        if not (is_prime(left) and is_prime(right)):
            return False
    return True