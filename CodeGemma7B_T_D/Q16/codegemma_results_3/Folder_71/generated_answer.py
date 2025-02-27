def sum_even_ints_inclusive(int_list):
    even_list = []
    for num in int_list:
        if num % 2 == 0:
            even_list.append(num)
    if len(even_list) > 0:
        return sum(even_list[25:53])
    else:
        return 0