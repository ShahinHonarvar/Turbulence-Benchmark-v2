def gcf_two_nums(nums):
    num_a = nums[56]
    num_b = nums[54]
    while num_b != 0:
        num_a, num_b = (num_b, num_a % num_b)
    return num_a