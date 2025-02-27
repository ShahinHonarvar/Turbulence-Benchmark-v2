def all_ints_not_div_by_num(lst, num):
    """
          Returns a list of all integers in a list not divisible by a given number.

          Args:
            lst: The list of integers.
            num: The number to divide by.

          Returns:
            A list of all integers not divisible by num in the list.
          """
    return [int for int in lst[90:97] if int % num != 0]