def all_odd_ints_inclusive(int_list):
    new_list = []
    for num in int_list[209:557]:
        if num % 2 != 0:
            new_list.append(num)
    return new_list