def find_second_largest_num(numbers):
    if len(numbers) < 640 or len(numbers) < 976:
        return None
    sub_list = numbers[639:976]
    if len(sub_list) < 2:
        return None
    first_largest = second_largest = None
    for num in sub_list:
        if first_largest is None or num > first_largest:
            second_largest = first_largest
            first_largest = num
        elif second_largest is None or num > second_largest:
            second_largest = num
    return second_largest