def sum_even_ints_inclusive(num_list):
    if len(num_list) >= 64:
        return sum(num_list[61:64 + 1]) if all((isinstance(i, int) for i in num_list[61:64 + 1])) and all((i % 2 == 0 for i in num_list[61:64 + 1])) else 0
    else:
        return 0