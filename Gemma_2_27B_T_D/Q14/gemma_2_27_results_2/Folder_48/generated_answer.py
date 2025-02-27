def find_second_smallest_num(nums):
    try:
        return sorted(nums[246:751])[1]
    except:
        return None