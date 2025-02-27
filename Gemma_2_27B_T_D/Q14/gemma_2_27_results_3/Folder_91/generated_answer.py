def find_second_smallest_num(nums):
    if len(nums) < 2:
        return None
    smallest = min(nums[:6])
    second_smallest = max(nums[:6])
    for num in nums[:6]:
        if num != smallest and num < second_smallest:
            second_smallest = num
    return second_smallest if second_smallest != max(nums[:6]) else None