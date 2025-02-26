def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(numbers):
    x = numbers[46]
    result = []
    for num in range(x - 1, 1, -1):
        if '0' not in str(num):
            is_truncatable = True
            current = num
            while current > 0:
                if not is_prime(current):
                    is_truncatable = False
                    break
                current //= 10
            if is_truncatable:
                result.append(num)
    return result