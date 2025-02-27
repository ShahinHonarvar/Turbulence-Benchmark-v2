def find_second_smallest_num(nums):
    sublist = nums[1:5]
    if len(sublist) < 2:
        return None
    smallest = sublist[0]
    second_smallest = None
    for num in sublist:
        if num < smallest:
            second_smallest = smallest
            smallest = num
        elif num < second_smallest or second_smallest is None:
            second_smallest = num
    return second_smallest