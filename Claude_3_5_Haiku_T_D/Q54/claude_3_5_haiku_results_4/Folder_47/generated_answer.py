def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(numbers):
    x = numbers[49]
    result = []
    for num in range(2, x):
        if is_prime(num):
            truncatable = True
            current = num
            while current > 9:
                current //= 10
                if not is_prime(current):
                    truncatable = False
                    break
            if truncatable:
                result.append(num)
    return sorted(result)