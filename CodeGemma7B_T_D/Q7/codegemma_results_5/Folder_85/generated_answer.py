def all_even_ints_inclusive(int_list):
    evens = []
    for num in int_list[6:9]:
        if num % 2 == 0:
            evens.append(num)
    return evens if evens else []