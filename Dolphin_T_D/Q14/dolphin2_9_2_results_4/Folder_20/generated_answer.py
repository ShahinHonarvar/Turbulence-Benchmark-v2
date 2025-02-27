def find_second_smallest_num(nums):
    sublist = nums[75:95]
    if len(sublist) < 2:
        return None
    smallest, second_smallest = (sublist[0], None)
    for num in sublist[1:]:
        if num < smallest:
            smallest, second_smallest = (num, smallest)
        elif second_smallest is None or num < second_smallest:
            second_smallest = num
    return second_smallest