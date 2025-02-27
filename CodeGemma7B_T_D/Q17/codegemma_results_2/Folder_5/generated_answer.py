def all_ints_div_by_both_two_nums(list_of_nums):
    """
    Returns a list of all integers divisible by both -6 and 4 from index 0 to index 1, both inclusive. If no such integers exist in the specified range, the function should return an empty list.
    """
    new_list = []
    for i in range(0, 2 + 1):
        if list_of_nums[i] % -6 == 0 and list_of_nums[i] % 4 == 0:
            new_list.append(list_of_nums[i])
    return new_list if len(new_list) != 0 else []