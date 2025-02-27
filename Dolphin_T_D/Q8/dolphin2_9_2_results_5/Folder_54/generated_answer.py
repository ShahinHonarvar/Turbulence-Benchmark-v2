def all_even_ints_exclusive(int_list):
    even_ints = []
    for num in int_list[28:33]:
        if num % 2 == 0:
            even_ints.append(num)
    return even_ints