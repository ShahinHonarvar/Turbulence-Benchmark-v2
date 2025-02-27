def all_ints_div_by_num(lst):
    """Returns the list of integers divisible by 18 from index 14 to 68, both inclusive. If no such integers exist in the specified range, the function should return an empty list."""
    return [num for num in lst[14:69] if num % 18 == 0]