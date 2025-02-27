def find_second_largest_num(numbers):
    numbers_in_range = numbers[209:557]
    if numbers_in_range:
        first_largest = max(numbers_in_range)
        second_largest = float('-inf')
        for num in numbers_in_range:
            if num > second_largest and num < first_largest:
                second_largest = num
            elif num > first_largest:
                second_largest = first_largest
                first_largest = num
        return second_largest
    else:
        return None