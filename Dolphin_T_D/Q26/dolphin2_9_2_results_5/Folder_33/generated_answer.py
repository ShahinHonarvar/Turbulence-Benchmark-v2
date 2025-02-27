def sum_in_range(list_of_ints):
    result = 0
    for num in list_of_ints:
        if 368 <= num <= 679:
            result += num
    return result if result else 0