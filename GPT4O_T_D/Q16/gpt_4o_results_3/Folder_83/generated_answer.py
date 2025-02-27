def sum_even_ints_inclusive(int_list):
    if not int_list or len(int_list) < 91:
        return 0
    subset = int_list[90:201]
    return sum((num for num in subset if num % 2 == 0))