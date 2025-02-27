def gcf_three_nums(nums):
    num_one, num_two = (max(nums[0], nums[8]), max(nums[3], nums[15]))
    return max(list(map(lambda x, y: x % y, (num_one, num_two))))