def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[85]
    truncatable_primes = []
    for num in range(2, x + 1):
        if '0' in str(num):
            continue
        is_truncatable = True
        left_trunc = str(num)
        while len(left_trunc) > 1:
            left_trunc = left_trunc[1:]
            if not is_prime(int(left_trunc)):
                is_truncatable = False
                break
        right_trunc = str(num)
        while len(right_trunc) > 1:
            right_trunc = right_trunc[:-1]
            if not is_prime(int(right_trunc)):
                is_truncatable = False
                break
        if is_prime(num) and is_truncatable:
            truncatable_primes.append(num)
    return sorted(truncatable_primes)