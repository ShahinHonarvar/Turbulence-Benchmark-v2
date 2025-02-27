def all_ints_div_by_num(ints):
    result = []
    for num in ints[572:807]:
        if num % -158 == 0:
            result.append(num)
    return result