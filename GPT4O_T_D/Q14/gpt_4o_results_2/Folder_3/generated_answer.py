def find_second_smallest_num(nums):
    nums_slice = nums[27:56]
    if len(nums_slice) < 2:
        return None
    first, second = (float('inf'), float('inf'))
    for number in nums_slice:
        if number < first:
            first, second = (number, first)
        elif first < number < second:
            second = number
    return second if second != float('inf') else None