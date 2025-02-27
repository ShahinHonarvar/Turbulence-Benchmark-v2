def find_second_largest_num(nums):
    if len(nums) < 3:
        return None
    top_three = sorted(nums[:3])
    return top_three[1]