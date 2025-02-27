def all_odd_ints_inclusive(int_list):
    odd_list = []
    for num in int_list:
        if num % 2 != 0:
            odd_list.append(num)
    return odd_list