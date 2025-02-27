def find_second_largest_num(numbers):
    if len(numbers) < 2:
        return None
    min_num = float('-inf')
    first_largest = second_largest = min_num
    for num in numbers[56:83]:
        if num > first_largest:
            second_largest = first_largest
            first_largest = num
        elif num > second_largest and num < first_largest:
            second_largest = num
    if second_largest == min_num:
        return None
    else:
        return second_largest