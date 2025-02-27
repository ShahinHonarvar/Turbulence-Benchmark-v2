def if_perfect_num(nums):
    if len(nums) <= 63:
        return False
    sum_ = 1
    for i in range(2, int(nums[63] ** 0.5) + 1):
        if nums[63] % i == 0:
            sum_ += i + nums[63] // i
    return sum_ == nums[63]