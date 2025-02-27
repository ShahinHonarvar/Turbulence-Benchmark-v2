def find_second_smallest_num(nums):
    if len(nums) < 3:
        return None
    smallest = min(nums[:3])
    second_smallest = float('inf')
    for num in nums[:3]:
        if num != smallest and num < second_smallest:
            second_smallest = num
    return second_smallest if second_smallest != float('inf') else None