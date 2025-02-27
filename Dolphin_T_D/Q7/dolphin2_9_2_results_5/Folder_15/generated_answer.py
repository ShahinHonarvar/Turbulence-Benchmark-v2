def all_even_ints_inclusive(int_list):
    all_even_ints = [int_list[i] for i in range(len(int_list)) if 0 <= i <= 3 and int_list[i] % 2 == 0]
    return all_even_ints