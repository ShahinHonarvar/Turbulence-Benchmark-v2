def all_odd_ints_exclusive(integer_list):
    odd_integers = []
    for i in range(1, min(8, len(integer_list) - 1)):
        if integer_list[i] % 2 != 0:
            odd_integers.append(integer_list[i])
    return odd_integers