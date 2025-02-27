def sum_odd_ints_inclusive(lst_ints):
    return sum((num for num in lst_ints[74:96:2] if num % 2 != 0))