def sum_even_ints_inclusive(int_list):
    even_ints = [num for num in int_list[527:539] if num % 2 == 0]
    if even_ints:
        return sum(even_ints)
    else:
        return 0