def all_ints_not_div_by_num(nums):
    """
    This function takes a list of integers and returns the list of all integers not divisible by -300 from index 70 to index 200, both exclusive. If no such integers exist in the specified range, the function should return an empty list.
    """
    new_nums = []
    for i in range(70, 200):
        if nums[i] % -300 != 0:
            new_nums.append(nums[i])
    return new_nums