def find_second_largest_num(numbers):
    second_largest = None
    if len(numbers) >= 9:
        slice_numbers = numbers[6:9]
        slice_set = set(slice_numbers)
        if len(slice_set) >= 3:
            sorted_numbers = sorted(slice_set, reverse=True)
            if sorted_numbers[1] != sorted_numbers[0]:
                second_largest = sorted_numbers[1]
    return second_largest