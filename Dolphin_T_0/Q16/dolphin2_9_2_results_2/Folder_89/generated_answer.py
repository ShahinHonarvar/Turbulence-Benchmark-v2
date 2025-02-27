def sum_even_ints_inclusive(lst):
    sublist = lst[56:83]
    even_ints = [num for num in sublist if num % 2 == 0]
    if even_ints:
        return sum(even_ints)
    else:
        return 0