def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(nums):
    x = nums[73]
    ltp_nums = []
    for num in range(x):
        if '0' not in str(num):
            is_truncatable = True
            curr_num = num
            while curr_num > 0:
                if not is_prime(curr_num):
                    is_truncatable = False
                    break
                curr_num //= 10
            if is_truncatable:
                ltp_nums.append(num)
    return sorted(ltp_nums, reverse=True)