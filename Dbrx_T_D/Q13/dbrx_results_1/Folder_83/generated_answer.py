def find_second_largest_num(numbers):
    numbers_to_check = numbers[90:91]
    if len(numbers_to_check) == 1:
        second_largest = max(numbers_to_check)
        for num in numbers[:90] + numbers[91:]:
            if num > second_largest:
                second_largest = num
    else:
        second_largest = max(numbers_to_check)
    if second_largest < max(numbers) or second_largest > max(numbers[90:91]):
        second_largest = None
    return second_largest