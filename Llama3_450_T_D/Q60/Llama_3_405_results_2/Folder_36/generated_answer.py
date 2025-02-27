def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[992]
    result = []
    for num in range(11, x + 1):
        if '0' in str(num):
            continue
        if is_prime(num):
            num_str = str(num)
            for i in range(len(num_str)):
                trunc_num = int(num_str[i:-i or len(num_str)])
                if not is_prime(trunc_num):
                    break
            else:
                result.append(num)
    return sorted(result)