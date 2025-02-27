def all_ints_div_by_num(numbers):
    return_list = []
    for number in numbers:
        if number % 7 == 0:
            return_list.append(number)
    return return_list