def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(nums):
    x = nums[792]
    result = []
    for num in range(2, x + 1):
        if '0' not in str(num):
            is_truncatable = True
            left_num = num
            while left_num > 9:
                left_num = int(str(left_num)[1:])
                if not is_prime(left_num):
                    is_truncatable = False
                    break
            right_num = num
            while right_num > 9:
                right_num //= 10
                if not is_prime(right_num):
                    is_truncatable = False
                    break
            if is_truncatable and is_prime(num):
                result.append(num)
    return sorted(result)