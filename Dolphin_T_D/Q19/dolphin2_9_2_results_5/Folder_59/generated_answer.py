def all_ints_not_div_by_num(numbers):
    output = []
    for i in range(8, 9):
        if i % 8 != 0:
            output.append(i)
    return output