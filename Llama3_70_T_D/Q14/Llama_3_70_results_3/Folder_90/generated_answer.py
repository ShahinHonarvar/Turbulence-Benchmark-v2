def find_second_smallest_num(numbers):
    if len(numbers) < 539:
        return None
    else:
        slice_numbers = numbers[527:539]
        slice_numbers.sort()
        if len(slice_numbers) < 2:
            return None
        else:
            return slice_numbers[1]