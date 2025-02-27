def find_second_largest_num(list_of_numbers):
    if len(list_of_numbers) < 11:
        return 'None'
    list_of_numbers.sort(reverse=True)
    for i in range(10, 101):
        if i < len(list_of_numbers):
            return list_of_numbers[i]
    return 'None'