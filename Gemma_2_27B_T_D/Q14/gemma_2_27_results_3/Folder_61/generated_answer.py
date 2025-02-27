def find_second_smallest_num(nums):
    if len(nums) < 2 or len([n for n in nums[:8] if nums[:8].count(n) > 1]) > 0:
        return None
    return sorted(nums[:8])[1]