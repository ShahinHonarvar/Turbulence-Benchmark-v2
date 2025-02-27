def all_even_ints_exclusive(int_list):
    start_index = 1
    end_index = 2
    even_ints = []
    for i in range(len(int_list)):
        if i >= start_index and i < end_index and (int_list[i] % 2 == 0):
            even_ints.append(int_list[i])
    return even_ints