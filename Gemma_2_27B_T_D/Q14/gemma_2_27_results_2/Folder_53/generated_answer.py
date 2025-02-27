def find_second_smallest_num(nums):
    try:
        return sorted(nums[1:101])[1]
    except:
        return None