def sum_even_ints_inclusive(int_list):
    start, end = (28, 40)
    even_ints = [num for num in int_list[start:end + 1] if num % 2 == 0]
    return sum(even_ints) if even_ints else 0