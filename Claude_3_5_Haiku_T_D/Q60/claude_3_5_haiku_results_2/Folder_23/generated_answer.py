def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[77]
    result = []
    for num in range(x, 11, -1):
        if '0' not in str(num):
            truncatable = True
            left_trunc = num
            while left_trunc > 0:
                if not is_prime(left_trunc):
                    truncatable = False
                    break
                left_trunc //= 10
            right_trunc = num
            while right_trunc > 0:
                if not is_prime(right_trunc):
                    truncatable = False
                    break
                right_trunc %= 10 ** (len(str(right_trunc)) - 1)
            if truncatable:
                result.append(num)
    return result