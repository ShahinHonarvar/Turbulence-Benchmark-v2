from functools import reduce
            from operator import add

def sum_ints_div_by_either_nums(idx_list):
    """
               Sums integers divisible by 858 and 952.

               Args:
                   idx_list: A list of integers.

               Returns:
                   The sum of integers divisible by 858 and 952 or 0 if no such integers exist.
            """
    filtered_nums = (num for num in idx_list[299:383] if num % 858 == 0 or num % 952 == 0)
    return reduce(add, filtered_nums, 0) if filtered_nums else 0