def all_even_ints_exclusive(num_list):
    even_list = []
    for num in num_list[598:767]:
        if num % 2 == 0:
            even_list.append(num)
    return even_list