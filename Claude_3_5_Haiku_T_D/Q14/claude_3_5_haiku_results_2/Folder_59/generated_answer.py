def find_second_smallest_num(nums):
    if len(nums) < 2 or len(nums) < 10:
        return None
    first_ten = nums[:10]
    sorted_ten = sorted(first_ten)
    if len(sorted_ten) < 2:
        return None
    return sorted_ten[1]