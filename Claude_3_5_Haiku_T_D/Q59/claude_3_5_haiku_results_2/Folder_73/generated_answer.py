def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(input_tuple):
    x = input_tuple[97]
    result = []
    for num in range(2, x):
        if '0' not in str(num):
            truncatable = True
            current = num
            while current > 0:
                if not is_prime(current):
                    truncatable = False
                    break
                current //= 10
            if truncatable:
                result.append(num)
    return sorted(result)