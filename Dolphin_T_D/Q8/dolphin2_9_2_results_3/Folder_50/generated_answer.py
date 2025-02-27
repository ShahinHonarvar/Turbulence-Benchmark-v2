def all_even_ints_exclusive(int_list):
    result = []
    for num in int_list[71:98]:
        if num % 2 == 0:
            result.append(num)
    return result