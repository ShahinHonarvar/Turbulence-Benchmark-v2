def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(numbers):
    x = numbers[30]
    result = []
    for num in range(2, x):
        if '0' not in str(num):
            is_left_truncatable = True
            current = num
            while current > 0:
                if not is_prime(current):
                    is_left_truncatable = False
                    break
                current = int(str(current)[1:]) if len(str(current)) > 1 else 0
            if is_left_truncatable:
                result.append(num)
    return sorted(result)