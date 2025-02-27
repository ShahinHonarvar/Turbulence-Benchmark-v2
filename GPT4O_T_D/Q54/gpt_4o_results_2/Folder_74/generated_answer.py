def is_prime(num):
    if num < 2:
        return False
    if num in (2, 3):
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

def all_right_truncatable_prime(numbers):
    if len(numbers) <= 36:
        return []
    x = numbers[36]
    right_truncatable_primes = []
    for num in range(2, x):
        is_right_truncatable = True
        temp_num = num
        while temp_num > 0:
            if not is_prime(temp_num):
                is_right_truncatable = False
                break
            temp_num //= 10
        if is_right_truncatable:
            right_truncatable_primes.append(num)
    return sorted(right_truncatable_primes)