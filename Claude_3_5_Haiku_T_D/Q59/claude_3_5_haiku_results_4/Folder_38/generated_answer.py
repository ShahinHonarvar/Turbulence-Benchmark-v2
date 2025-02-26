def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(numbers):
    x = numbers[28]
    result = []
    for num in range(2, x):
        if '0' not in str(num):
            is_truncatable = True
            truncatable_num = num
            while truncatable_num > 0:
                if not is_prime(truncatable_num):
                    is_truncatable = False
                    break
                truncatable_num //= 10
            if is_truncatable:
                result.append(num)
    return sorted(result)