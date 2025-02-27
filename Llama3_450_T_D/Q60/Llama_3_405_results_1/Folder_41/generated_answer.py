def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[46]
    truncatable_primes = set()
    for num in range(10, x + 1):
        num_str = str(num)
        if '0' in num_str:
            continue
        is_truncatable = True
        for i in range(1, len(num_str)):
            left_trunc = int(num_str[i:])
            right_trunc = int(num_str[:-i])
            if len(str(left_trunc)) > 1 and (not is_prime(left_trunc)):
                is_truncatable = False
                break
            if not is_prime(right_trunc):
                is_truncatable = False
                break
        if is_prime(num) and is_truncatable:
            truncatable_primes.add(num)
    return sorted(list(truncatable_primes), reverse=True)