def find_second_smallest_num(nums):
    if len(nums) < 6:
        return 'None'
    second_smallest = float('inf')
    for i in range(3, 6):
        if nums[i] < second_smallest:
            second_smallest = nums[i]
    return second_smallest if second_smallest != float('inf') else 'None'