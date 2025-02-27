def sum_ints_div_by_either_nums(nums):
    """
    Sums all integers in the list that are divisible by either -90 or -74 from index 42 to index 87, inclusive.
    """
    sum = 0
    for num in nums[42:88]:
        if num % 90 == 0 or num % 74 == 0:
            sum += num
    return sum if sum else 0