def all_ints_not_div_by_num(lst):
    """
            Returns the list of all integers not divisible by 1000 from index 80 to index 200, both exclusive.
            If no such integers exist in the specified range, the function should return an empty list.
            """
    return [i for i in lst[80:200] if i % 1000]