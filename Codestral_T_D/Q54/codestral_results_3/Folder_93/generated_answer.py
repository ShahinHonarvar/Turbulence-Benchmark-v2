def all_right_truncatable_prime(numbers):
    x = numbers[11]
    result = []
    for num in range(2, x):
        if is_prime(num):
            truncated = num
            while truncated > 0:
                truncated = truncated // 10
                if not is_prime(truncated):
                    break
            else:
                result.append(num)
    return sorted(result)

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True