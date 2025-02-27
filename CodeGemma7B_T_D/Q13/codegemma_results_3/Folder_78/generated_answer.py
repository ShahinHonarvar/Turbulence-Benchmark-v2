def find_second_largest_num(numbers):
    largest = max(numbers)
    smaller_numbers = [num for num in numbers if num != largest]
    second_largest = max(smaller_numbers)
    if 43 <= second_largest <= 51:
        return second_largest
    else:
        return 'None'