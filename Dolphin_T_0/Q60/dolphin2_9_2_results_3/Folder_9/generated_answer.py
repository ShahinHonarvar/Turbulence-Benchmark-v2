def all_left_right_truncatable_prime(int_tuple):
    x = int_tuple[29]
    result = []
    for num in range(x, 1, -1):
        if is_prime(num):
            num_str = str(num)
            if '0' in num_str or not is_prime(int(num_str[1:-1])):
                continue
            left_flag = True
            right_flag = True
            while num_str:
                if is_prime(int(num_str)):
                    num_str = num_str[1:-1]
                else:
                    left_flag = False
                    break
            while num_str[::-1]:
                if is_prime(int(num_str[::-1])):
                    num_str = num_str[1:-1]
                else:
                    right_flag = False
                    break
            if left_flag and right_flag:
                result.append(num)
    return result

def is_prime(n):
    if n == 2:
        return True
    if n < 2 or n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True