def sum_even_ints_inclusive(int_list):
    start, end = (62, 92)
    return sum((num for num in int_list[start:end + 1] if num % 2 == 0)) if sum(list(map(lambda x: 1 if x % 2 == 0 else 0, int_list[start:end + 1]))) > 0 else 0