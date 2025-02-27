def find_second_largest_num(numbers):
    if len(numbers) < 2 or len(numbers) < 637:
        return None
    second_largest = None
    largest = max((numbers[index] for index in range(639, 976)))
    for num in numbers[639:976]:
        if num > second_largest and num < largest:
            second_largest = num
    return second_largest