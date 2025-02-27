def find_second_largest_num(nums):
    try:
        return sorted(nums[91:100])[-2]
    except:
        return None