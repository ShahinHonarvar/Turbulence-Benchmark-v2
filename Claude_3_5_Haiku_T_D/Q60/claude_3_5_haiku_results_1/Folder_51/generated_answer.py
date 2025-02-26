def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(nums):
    x = nums[54]
    result = []
    for num in range(2, x + 1):
        if '0' not in str(num):
            is_truncatable = True
            left = str(num)
            right = str(num)
            while len(left) > 1:
                left = left[1:]
                if not is_prime(int(left)):
                    is_truncatable = False
                    break
            while len(right) > 1:
                right = right[:-1]
                if not is_prime(int(right)):
                    is_truncatable = False
                    break
            if is_truncatable and is_prime(num):
                result.append(num)
    return sorted(result)