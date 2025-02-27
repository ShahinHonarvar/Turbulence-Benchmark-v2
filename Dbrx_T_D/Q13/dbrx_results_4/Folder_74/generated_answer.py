def find_second_largest_num(numbers):
    second_largest = None
    if len(numbers) >= 62:
        numbers = numbers[17:79]
        unique_numbers = list(set(numbers))
        if len(unique_numbers) >= 2:
            unique_numbers.sort(reverse=True)
            second_largest = unique_numbers[1]
    return second_largest