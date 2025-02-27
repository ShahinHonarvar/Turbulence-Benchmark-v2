def all_ints_div_by_num(int_list):
    result = []
    for number in int_list[572:807]:
        if number % -158 == 0:
            result.append(number)
    return result