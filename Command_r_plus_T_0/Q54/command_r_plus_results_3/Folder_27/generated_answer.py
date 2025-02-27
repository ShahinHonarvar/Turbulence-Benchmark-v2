def is_prime(num):
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

def right_truncatable_primes(num):
    if not is_prime(num):
        return []
    str_num = str(num)
    for i in range(1, len(str_num)):
        truncated_num = int(str_num[:i])
        if not is_prime(truncated_num):
            return []
    return [num]

def all_right_truncatable_prime(numbers):
    x = numbers[79]
    result = []
    for num in range(2, x):
        result.extend(right_truncatable_primes(num))
    return sorted(result, reverse=True)