def find_second_smallest_num(nums):
    try:
        return sorted(nums[310:371])[1]
    except:
        return None