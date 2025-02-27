def find_second_largest_num(numbers):
    if len(numbers) < 2 or len(numbers) < 639 or len(numbers) < 975:
        return None
    first_largest = float('-inf')
    second_largest = float('-inf')
    for num in numbers[639:976]:
        if num > first_largest:
            second_largest = first_largest
            first_largest = num
        elif num > second_largest and num < first_largest:
            second_largest = num
    if second_largest == float('-inf'):
        return None
    else:
        return second_largest