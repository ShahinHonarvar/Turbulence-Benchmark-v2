def find_second_largest_num(numbers):
    sub_list = numbers[42:69]
    if len(sub_list) < 2:
        return None
    first_largest = second_largest = float('-inf')
    for num in sub_list:
        if num > first_largest:
            second_largest = first_largest
            first_largest = num
        elif num > second_largest:
            second_largest = num
    return second_largest if second_largest != float('-inf') else None