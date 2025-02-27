def sum_ints_div_by_either_nums(nums):
    """
            Returns the sum of all integers divisible by either 55 or 10 from index 58 to index 81, both inclusive.
            """
    output = 0
    for i in range(58, 82):
        if nums[i] % 55 == 0 or nums[i] % 10 == 0:
            output += nums[i]
        i += 1
    return output if nums[i] >= 58 else 0