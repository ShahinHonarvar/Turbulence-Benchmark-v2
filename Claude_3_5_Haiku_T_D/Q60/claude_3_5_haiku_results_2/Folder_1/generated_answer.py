def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(nums):
    x = nums[20]
    result = []
    for num in range(x, 11, -1):
        if '0' not in str(num):
            is_truncatable = True
            current_num = num
            while len(str(current_num)) > 1:
                current_num //= 10
                if not is_prime(current_num):
                    is_truncatable = False
                    break
            if is_truncatable:
                current_num = num
                while len(str(current_num)) > 1:
                    current_num = int(str(current_num)[1:])
                    if not is_prime(current_num):
                        is_truncatable = False
                        break
            if is_truncatable and is_prime(num):
                result.append(num)
    return result