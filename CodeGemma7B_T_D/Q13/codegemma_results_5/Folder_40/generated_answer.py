def find_second_largest_num(dist_nums):
    if len(dist_nums) < 3:
        return 'None'
    nums = dist_nums[:3]
    nums.sort(reverse=True)
    return nums[1]