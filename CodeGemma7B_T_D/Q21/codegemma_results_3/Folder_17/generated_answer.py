def all_ints_div_by_num(int_list):
    """
            Returns the list of all integers divisible by 91 from index 33 to index 35, both inclusive.

            Args:
                int_list: A list of integers.

            Returns:
                A list of integers divisible by 91 from index 33 to index 35, both inclusive. If no such integers exist, the function returns an empty list.
            """
    divisible_nums = []
    for num in int_list:
        if num % 91 == 0 and 33 <= int_list.index(num) <= 35:
            divisible_nums.append(num)
    return divisible_nums