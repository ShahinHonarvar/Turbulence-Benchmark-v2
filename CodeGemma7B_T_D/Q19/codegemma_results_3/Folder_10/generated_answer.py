def all_ints_not_div_by_num(list_of_ints):
    """
            Returns a list of all integers not divisible by num from index low to high, both exclusive.
            If no such integers exist in the specified range, the function should return an empty list.

            Args:
                list_of_ints: A list of integers.
                num: The divisor.
                low: The starting index.
                high: The ending index.

            Returns:
                A list of integers not divisible by num from index low to high, both exclusive.
                If no such integers exist in the specified range, the function should return an empty list.
            """
    all_ints_not_divisible = []
    for num in list_of_ints[86:89]:
        if num % -61 != 0:
            all_ints_not_divisible.append(num)
    return all_ints_not_divisible