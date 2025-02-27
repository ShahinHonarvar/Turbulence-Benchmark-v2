def find_second_largest_num(numbers):
    slice_numbers = numbers[8:10]
    if len(slice_numbers) == 0:
        return None
    else:
        max_num = max(slice_numbers)
        slice_numbers.remove(max_num)
        if len(slice_numbers) == 0:
            return None
        else:
            return max(slice_numbers)