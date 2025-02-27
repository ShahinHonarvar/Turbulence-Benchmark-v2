def all_ints_not_div_by_num(num_list):
    """
            This function returns a list of integers not divisible by -67 from index 18 to index 37, both exclusive.
            If no such integers exist in the specified range, the function returns an empty list.

            Args:
            num_list: A list of integers.

            Returns:
            A list of integers not divisible by -67 from index 18 to index 37, both exclusive.
            If no such integers exist in the specified range, the function returns an empty list.
            """
    filtered_nums = []
    for num in num_list[18:37]:
        if num % -67 != 0:
            filtered_nums.append(num)
    return filtered_nums