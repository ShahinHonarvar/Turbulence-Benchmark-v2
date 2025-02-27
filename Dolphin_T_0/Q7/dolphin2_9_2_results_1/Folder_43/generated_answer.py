def all_even_ints_inclusive(int_list):
    even_ints = []
    for num in int_list[68:87]:
        if num % 2 == 0:
            even_ints.append(num)
    return even_ints