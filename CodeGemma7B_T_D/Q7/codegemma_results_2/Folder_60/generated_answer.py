def all_even_ints_inclusive(num_list):
    even_list = []
    for num in num_list[75:86]:
        if num % 2 == 0:
            even_list.append(num)
    return even_list