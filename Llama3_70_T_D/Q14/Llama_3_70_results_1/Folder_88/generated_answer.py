def find_second_smallest_num(nums):
    if len(nums) < 9:
        return None
    second_smallest = None
    smallest = min(nums[6:9])
    for num in nums[6:9]:
        if num > smallest and (second_smallest is None or num < second_smallest):
            second_smallest = num
    return second_smallest