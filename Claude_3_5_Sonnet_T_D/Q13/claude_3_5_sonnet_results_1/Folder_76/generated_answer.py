def find_second_largest_num(numbers):
    sub_list = numbers[686:988]
    if len(sub_list) < 2:
        return None
    largest = max(sub_list)
    second_largest = max((num for num in sub_list if num != largest))
    return second_largest if second_largest != largest else None