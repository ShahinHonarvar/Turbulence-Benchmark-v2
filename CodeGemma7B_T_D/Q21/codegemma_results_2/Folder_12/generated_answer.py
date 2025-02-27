def all_ints_div_by_num(nums):
    """
            This function takes one argument, a list of integers, and returns the list of all integers divisible by -46 from index 23 to index 65, both inclusive. If no such integers exist in the specified range, the function should return an empty list.
            """
    result = []
    for num in nums[23:66]:
        if num % -46 == 0 and num != 0:
            result.append(num)
    return result