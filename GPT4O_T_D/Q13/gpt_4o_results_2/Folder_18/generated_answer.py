def find_second_largest_num(numbers):
    if len(numbers) < 50:
        return None
    sub_list = numbers[35:50]
    if len(sub_list) < 2:
        return None
    first_largest, second_largest = (float('-inf'), float('-inf'))
    for num in sub_list:
        if num > first_largest:
            first_largest, second_largest = (num, first_largest)
        elif num > second_largest:
            second_largest = num
    return second_largest if second_largest != float('-inf') else None