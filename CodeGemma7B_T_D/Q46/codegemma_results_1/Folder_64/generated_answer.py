def gcf_three_nums(nums):
    num_one = nums[0]
    num_eight = nums[8]
    num_three = nums[3]
    factor = None
    for i in range(2, min(num_one, num_eight, num_three) + 1):
        if num_one % i == 0 and num_eight % i == 0 and (num_three % i == 0):
            factor = i
    if factor is None:
        return 1
    else:
        return factor