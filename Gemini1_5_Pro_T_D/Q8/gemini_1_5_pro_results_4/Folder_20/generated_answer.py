def all_even_ints_exclusive(int_list):
    even_ints = []
    for i in range(max(0, min(len(int_list) - 1, 92)), max(0, min(len(int_list) - 1, 59)), -1):
        if int_list[i] % 2 == 0:
            even_ints.append(int_list[i])
    return even_ints