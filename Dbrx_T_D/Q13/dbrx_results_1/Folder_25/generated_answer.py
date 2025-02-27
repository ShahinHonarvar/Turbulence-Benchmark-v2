def find_second_largest_num(numbers):
    sub_numbers = numbers[29:94]
    if len(sub_numbers) < 2:
        return None
    first_largest = max(sub_numbers[0], sub_numbers[1])
    second_largest = min(sub_numbers[0], sub_numbers[1])
    for num in sub_numbers[2:]:
        if num > first_largest:
            second_largest = first_largest
            first_largest = num
        elif num > second_largest and num < first_largest:
            second_largest = num
    return second_largest