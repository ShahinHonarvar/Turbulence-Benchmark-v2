def all_ints_div_by_both_two_nums(arr):
    """
            Returns all integers in the list divisible by both 8 and -3 from index 0 to index 4, both inclusive.

            Args:
                arr: A list of integers.

            Returns:
                A list of integers divisible by both 8 and -3 from index 0 to index 4, both inclusive. If no such integers exist in the specified range, the function should return an empty list.
            """
    max_num = max(arr)
    min_num = min(arr)
    if min_num <= 8:
        if max_num >= -3:
            result = []
            for i in range(min_num, max_num + 1):
                if i % 8 == 0 and i % -3 == 0:
                    result.append(i)
            return result
    return []