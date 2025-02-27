def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[29]
    result = []
    for num in range(10, x + 1):
        num_str = str(num)
        if '0' in num_str:
            continue
        left_right_truncatable = True
        for i in range(len(num_str)):
            truncated_num = int(num_str[i:])
            if not is_prime(truncated_num):
                left_right_truncatable = False
                break
            if len(num_str) - i > 1:
                truncated_num = int(num_str[i:-1])
                if not is_prime(truncated_num):
                    left_right_truncatable = False
                    break
        if left_right_truncatable:
            result.append(num)
    return sorted(result)