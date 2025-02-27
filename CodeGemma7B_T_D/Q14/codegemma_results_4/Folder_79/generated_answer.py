def find_second_smallest_num(nums):
    if not nums:
        return None
    second_lowest = float('inf')
    lowest = float('inf')
    for num in nums:
        if num < lowest:
            lowest = num
    for num in nums:
        if num < second_lowest and num != lowest:
            second_lowest = num
    return second_lowest