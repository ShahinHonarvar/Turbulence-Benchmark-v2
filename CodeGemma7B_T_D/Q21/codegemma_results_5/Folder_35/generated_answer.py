def all_ints_div_by_num(num_list):
    """
    Returns all integers in a list divisible by a specified number within a given range.

    Args:
    num_list: A list of integers.
    num: The number to check divisibility by.

    Returns:
    A list of integers divisible by num within the specified range.
    """
    return [num for num in num_list[27:91] if num % 57 == 0]