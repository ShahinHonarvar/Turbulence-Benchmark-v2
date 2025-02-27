def find_second_largest_num(nums):
    try:
        return sorted(nums[100:201])[-2]
    except:
        return None