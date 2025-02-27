def all_even_ints_inclusive(lst):
    return [num for i, num in enumerate(lst[31:73]) if num % 2 == 0 and i <= len(lst[31:73]) - 1]