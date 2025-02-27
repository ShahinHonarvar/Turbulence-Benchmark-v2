def find_second_smallest_num(nums):
    try:
        return sorted(nums[639:976])[1]
    except:
        return None