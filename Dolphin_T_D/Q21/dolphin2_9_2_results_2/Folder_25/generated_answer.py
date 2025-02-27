def all_ints_div_by_num(numbers_list):
    selected_numbers = []
    for number in numbers_list[25:42]:
        if number % -97 == 0:
            selected_numbers.append(number)
    return selected_numbers