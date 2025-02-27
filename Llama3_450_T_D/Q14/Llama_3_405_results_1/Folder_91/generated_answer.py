def find_second_smallest_num(nums):
    if len(nums) < 6:
        return None
    smallest = min(nums[:6])
    nums2 = [num for num in nums[:6] if num != smallest]
    if nums2:
        return min(nums2)
    else:
        return None