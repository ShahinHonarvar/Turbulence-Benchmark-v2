def find_second_largest_num(numbers):
    if len(numbers) < 80:
        return None
    else:
        slice_numbers = numbers[29:80]
        sorted_numbers = sorted(slice_numbers, reverse=True)
        if len(sorted_numbers) < 2:
            return None
        else:
            return sorted_numbers[1]