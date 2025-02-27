def find_second_largest_num(list_of_numbers):
    if min(list_of_numbers[100:201]) == max(list_of_numbers[100:201]):
        return None
    first = max(list_of_numbers[100:201])
    list_of_numbers[100:201].remove(first)
    if len(list_of_numbers[100:201]) < 2:
        return None
    second = max(list_of_numbers[100:201])
    return second