def find_second_smallest_num(nums):
    if len(nums) < 7:
        return None
    else:
        temp = sorted(nums[0:7])
        return temp[1]