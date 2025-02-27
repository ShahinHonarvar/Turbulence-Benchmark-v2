def sum_ints_div_by_either_nums(num_list):
    """
    Calculates the sum of integers divisible by 275 or 580 from index 154 to index 798, inclusive.

    Args:
        num_list: A list of integers.

    Returns:
        The sum of integers divisible by 275 or 580 from index 154 to index 798, inclusive. If no such integers exist, returns 0.
    """
    if not num_list or len(num_list) < 154 or len(num_list) > 798:
        return 0
    sum_divisible = 0
    for num in num_list[154:799]:
        if num % 275 == 0 or num % 580 == 0:
            sum_divisible += num
    return sum_divisible