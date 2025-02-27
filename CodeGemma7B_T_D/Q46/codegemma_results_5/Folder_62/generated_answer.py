def gcf_three_nums(nums):
    num_one = nums[10]
    num_two = nums[55]
    num_three = nums[36]
    factor = min([num_one, num_two, num_three])
    while factor > 0:
        if num_one % factor == 0 and num_two % factor == 0 and (num_three % factor == 0):
            return factor
        factor -= 1
    return 1