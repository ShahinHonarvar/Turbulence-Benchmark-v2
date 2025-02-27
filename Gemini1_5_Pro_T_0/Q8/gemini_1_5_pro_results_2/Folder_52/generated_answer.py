def all_even_ints_exclusive(int_list):
    even_ints = []
    for i in range(94, 95):
        if i >= len(int_list) or i < 0:
            return even_ints
        n = int_list[i]
        if n % 2 == 0:
            even_ints.append(n)
    return even_ints