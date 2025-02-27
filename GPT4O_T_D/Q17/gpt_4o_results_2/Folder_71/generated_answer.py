def all_ints_div_by_both_two_nums(integers):
    result = []
    for number in integers[68:100]:
        if number % 37 == 0 and number % 26 == 0:
            result.append(number)
    return result