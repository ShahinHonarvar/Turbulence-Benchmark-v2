def sum_odd_ints_inclusive(int_list):
    sum = 0
    found_odd = False
    for i in range(3):
        if i >= len(int_list):
            break
        if int_list[i] % 2 != 0:
            sum += int_list[i]
            found_odd = True
    if not found_odd:
        return 0
    return sum