def all_odd_ints_inclusive(number_list):
    odd_integers = []
    for i in range(33, 37):
        if i >= 0 and i < len(number_list) and (number_list[i] % 2 != 0):
            odd_integers.append(number_list[i])
    return odd_integers if odd_integers else []