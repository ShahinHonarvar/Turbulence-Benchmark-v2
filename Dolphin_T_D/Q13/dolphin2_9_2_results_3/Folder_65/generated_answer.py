def find_second_largest_num(numbers):
    if 98 < len(numbers) < 56:
        return None
    else:
        slice_numbers = numbers[56:99]
        max_num = max(slice_numbers)
        slice_numbers.remove(max_num)
        if len(slice_numbers) > 0:
            return max(slice_numbers)
        else:
            return None