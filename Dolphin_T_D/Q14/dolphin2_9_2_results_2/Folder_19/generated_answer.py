def find_second_smallest_num(nums):
    if not 4 <= len(nums) <= 8:
        return None
    second_smallest = float('inf')
    smallest = float('inf')
    for num in nums[4:9]:
        if num < smallest:
            second_smallest = smallest
            smallest = num
        elif num < second_smallest:
            second_smallest = num
    return second_smallest if second_smallest != float('inf') else None