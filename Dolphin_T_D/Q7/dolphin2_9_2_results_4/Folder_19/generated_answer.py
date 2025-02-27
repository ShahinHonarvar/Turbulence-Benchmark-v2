def all_even_ints_inclusive(lst):
    even_list = []
    for number in lst[3:6]:
        if number % 2 == 0:
            even_list.append(number)
    return even_list