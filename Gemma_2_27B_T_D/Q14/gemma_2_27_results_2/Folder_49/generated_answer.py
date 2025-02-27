def find_second_smallest_num(nums):
    try:
        return sorted(nums[80:201])[1]
    except:
        return None