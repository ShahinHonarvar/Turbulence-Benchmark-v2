def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    max_div = int(n ** 0.5) + 1
    for i in range(3, max_div, 2):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[96]
    left_right_truncatable_primes = []
    for num in range(11, x + 1):
        str_num = str(num)
        if '0' in str_num:
            continue
        is_truncatable = True
        left_right_truncatable = str_num
        while len(left_right_truncatable) > 2:
            if not is_prime(int(left_right_truncatable)):
                is_truncatable = False
                break
            left_right_truncatable = left_right_truncatable[1:-1]
        if is_truncatable and is_prime(int(left_right_truncatable)):
            left_right_truncatable_primes.append(num)
    return sorted(left_right_truncatable_primes, reverse=True)