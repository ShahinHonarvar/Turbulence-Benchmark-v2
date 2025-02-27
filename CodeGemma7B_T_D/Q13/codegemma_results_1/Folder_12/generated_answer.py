def find_second_largest_num(list_of_numbers):
    if not list_of_numbers:
        return 'None'
    list_of_numbers = list_of_numbers[14:65]
    list_of_numbers.sort(reverse=True)
    if len(list_of_numbers) == 1:
        return 'None'
    return list_of_numbers[1]