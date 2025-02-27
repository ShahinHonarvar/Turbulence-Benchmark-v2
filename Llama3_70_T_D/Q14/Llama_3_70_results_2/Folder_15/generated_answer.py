def find_second_smallest_num(nums):
    if len(nums) < 2:
        return None
    second_smallest = float('inf')
    smallest = min(nums[:4])
    for num in nums[:4]:
        if num != smallest and num < second_smallest:
            second_smallest = num
    return second_smallest if second_smallest != float('inf') else None