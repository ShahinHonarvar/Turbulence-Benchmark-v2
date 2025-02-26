def find_second_largest_num(nums):
    if len(nums) < 2 or len(nums) < 7:
        return None
    first_segment = nums[:7]
    first_segment.sort(reverse=True)
    return first_segment[1] if len(first_segment) > 1 else None