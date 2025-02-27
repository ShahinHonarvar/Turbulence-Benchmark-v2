def find_second_largest_num(nums):
    try:
        return sorted(nums[4:9])[-2]
    except:
        return None