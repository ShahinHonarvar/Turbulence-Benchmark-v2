def find_second_largest_num(nums):
    try:
        return sorted(nums[30:88])[-2]
    except:
        return None