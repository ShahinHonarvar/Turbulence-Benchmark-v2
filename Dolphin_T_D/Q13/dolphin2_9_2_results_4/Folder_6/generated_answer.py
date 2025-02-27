def find_second_largest_num(numbers):
    second_largest = None
    for num in numbers[66:10:-1]:
        if second_largest is None or num > second_largest:
            second_largest = num
        elif second_largest is not None and num != second_largest:
            return num
    return second_largest