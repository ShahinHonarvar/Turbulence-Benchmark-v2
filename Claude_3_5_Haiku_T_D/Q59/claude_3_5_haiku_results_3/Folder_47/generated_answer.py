def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(input_tuple):
    x = input_tuple[49]
    result = []
    for num in range(2, x):
        if '0' not in str(num):
            is_truncatable = True
            truncated_num = num
            while len(str(truncated_num)) > 1:
                truncated_num = int(str(truncated_num)[1:])
                if not is_prime(truncated_num):
                    is_truncatable = False
                    break
            if is_truncatable and is_prime(num):
                result.append(num)
    return sorted(result)