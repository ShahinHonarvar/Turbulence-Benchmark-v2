def find_second_largest_num(nums):
    if len(nums) > 78:
        try:
            return sorted(nums[62:79])[-2]
        except IndexError:
            return None
    else:
        return None