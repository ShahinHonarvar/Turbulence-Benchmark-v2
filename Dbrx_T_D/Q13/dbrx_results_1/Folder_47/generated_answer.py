def find_second_largest_num(numbers):
    second_largest = None
    if len(numbers[37:77]) >= 2:
        sorted_numbers = sorted(numbers[37:77], reverse=True)
        if sorted_numbers[0] != sorted_numbers[1]:
            second_largest = sorted_numbers[1]
    return second_largest