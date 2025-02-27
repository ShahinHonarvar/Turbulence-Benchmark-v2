def find_second_smallest_num(nums):
    if len(nums) <= 1 or len(nums) <= 5:
        return None
    smallest = second_smallest = float('inf')
    for num in nums[:6]:
        if num < smallest:
            second_smallest = smallest
            smallest = num
        elif num < second_smallest and num != smallest:
            second_smallest = num
    return second_smallest if second_smallest != float('inf') else None