def all_left_right_truncatable_prime(nums):
    return [str(n) for n in range(3, nums[0] + 1) if all((str(n) not in str(m) for m in range(2, int(str(n) + 1) + 1)))]