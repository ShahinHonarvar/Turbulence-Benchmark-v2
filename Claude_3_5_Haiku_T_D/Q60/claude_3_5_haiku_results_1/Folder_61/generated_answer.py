def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[3]
    result = []
    for num in range(x, 11, -1):
        if '0' in str(num):
            continue
        is_truncatable = True
        temp_num_left = num
        temp_num_right = num
        while temp_num_left > 0 and is_truncatable:
            if not is_prime(temp_num_left):
                is_truncatable = False
                break
            temp_num_left //= 10
        while temp_num_right > 0 and is_truncatable:
            if not is_prime(temp_num_right):
                is_truncatable = False
                break
            temp_num_right %= 10 ** (len(str(temp_num_right)) - 1)
        if is_truncatable and temp_num_left == 0 and (temp_num_right == 0):
            result.append(num)
    return result