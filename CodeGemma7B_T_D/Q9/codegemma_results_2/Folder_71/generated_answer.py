def all_odd_ints_inclusive(int_list):
    odd_list = []
    for num in int_list[26:53]:
        if num % 2 != 0:
            odd_list.append(num)
    return odd_list if odd_list else []