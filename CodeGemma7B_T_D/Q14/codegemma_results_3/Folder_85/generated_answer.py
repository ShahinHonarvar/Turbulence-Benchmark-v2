def find_second_smallest_num(nums):
    second_smallest = float('inf')
    for num in nums:
        if num < second_smallest and num > nums[0]:
            second_smallest = num
    return second_smallest if second_smallest != float('inf') else 'None'