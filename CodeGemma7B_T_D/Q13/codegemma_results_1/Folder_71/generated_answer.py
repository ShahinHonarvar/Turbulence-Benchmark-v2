def find_second_largest_num(list_of_numbers):
    list_of_numbers.sort(reverse=True)
    if len(list_of_numbers[26:53]) >= 2:
        return list_of_numbers[27]
    else:
        return 'None'