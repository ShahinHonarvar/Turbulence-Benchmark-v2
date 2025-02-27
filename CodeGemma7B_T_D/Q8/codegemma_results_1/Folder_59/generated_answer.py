def all_even_ints_exclusive(int_list):
    even_ints = []
    for num in int_list:
        if num % 2 == 0 and num >= 0 and (num <= 9):
            even_ints.append(num)
    return even_ints