def find_second_largest_num(numbers):
    if len(numbers) < 60:
        return None
    sub_list = numbers[25:60]
    if len(sub_list) < 2:
        return None
    largest = max(sub_list)
    second_largest = max((num for num in sub_list if num != largest))
    return second_largest