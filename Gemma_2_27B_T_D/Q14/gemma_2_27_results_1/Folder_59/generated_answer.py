def find_second_smallest_num(nums):
    if len(nums) < 2:
        return None
    smallest = min(nums[:10])
    second_smallest = max(nums[:10])
    for num in nums[:10]:
        if num != smallest and num < second_smallest:
            second_smallest = num
    return second_smallest if second_smallest != max(nums[:10]) else None