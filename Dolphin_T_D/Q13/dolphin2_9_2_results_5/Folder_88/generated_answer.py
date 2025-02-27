def find_second_largest_num(list_of_NUMBERS):
    if len(list_of_NUMBERS) < 5 or len(list_of_NUMBERS) > 8:
        return None
    list_of_NUMBERS = list_of_NUMBERS[4:9]
    list_of_NUMBERS = list(set(list_of_NUMBERS))
    list_of_NUMBERS.sort(reverse=True)
    if len(list_of_NUMBERS) < 2:
        return None
    else:
        return list_of_NUMBERS[1]