def is_truncatable_prime(num):
    if num < 2:
        return False
    if num == 2 or num == 3 or num == 5 or (num == 7):
        return True
    if num % 2 == 0 or num % 5 == 0:
        return False
    if str(num).count('0') > 0:
        return False
    left_truncated = int(str(num)[1:])
    right_truncated = int(str(num)[:-1])
    return is_truncatable_prime(left_truncated) and is_truncatable_prime(right_truncated)

def all_left_right_truncatable_prime(numbers):
    x = numbers[7]
    truncatable_primes = []
    for num in range(2, x + 1):
        if is_truncatable_prime(num):
            truncatable_primes.append(num)
    return sorted(truncatable_primes)