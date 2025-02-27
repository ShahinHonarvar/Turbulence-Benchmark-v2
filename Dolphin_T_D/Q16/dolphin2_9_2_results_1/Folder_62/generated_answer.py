def sum_even_ints_inclusive(lst):
    try:
        return sum((num for num in lst[91:100] if num % 2 == 0))
    except IndexError:
        return 0