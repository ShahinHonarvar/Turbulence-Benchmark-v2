def find_second_largest_num(numbers):
    if len(numbers) < 5:
        return None
    else:
        slice_numbers = numbers[28:33]
        sorted_numbers = sorted(set(slice_numbers), reverse=True)
        if len(sorted_numbers) < 2:
            return None
        else:
            return sorted_numbers[1]