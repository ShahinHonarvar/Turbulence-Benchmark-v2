def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(nums):
    x = nums[78]
    result = []
    for num in range(x, 11, -1):
        if '0' in str(num):
            continue
        is_truncatable = True
        n_str = str(num)
        while len(n_str) > 1:
            n_str = n_str[1:-1]
            if not is_prime(int(n_str)):
                is_truncatable = False
                break
        left_check = str(num)
        right_check = str(num)
        while len(left_check) > 1:
            left_check = left_check[1:]
            right_check = right_check[:-1]
            if not (is_prime(int(left_check)) and is_prime(int(right_check))):
                is_truncatable = False
                break
        if is_truncatable and is_prime(num):
            result.append(num)
    return result