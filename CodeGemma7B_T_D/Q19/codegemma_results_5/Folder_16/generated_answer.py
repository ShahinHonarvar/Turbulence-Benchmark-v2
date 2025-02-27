def all_ints_not_div_by_num(nums):
    """Function to return all integers not divisible by 35 from index 24 to index 32, both exclusive."""
    res = []
    for num in nums[24:32]:
        if num % 35 != 0:
            res.append(num)
    return res