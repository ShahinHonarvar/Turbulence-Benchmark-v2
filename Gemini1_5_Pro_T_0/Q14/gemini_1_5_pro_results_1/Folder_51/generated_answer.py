def find_second_smallest_num(numbers):
    if len(numbers) < 9:
        return None
    else:
        sliced_numbers = numbers[1:9]
        sorted_numbers = sorted(sliced_numbers)
        if len(sorted_numbers) < 2:
            return None
        else:
            return sorted_numbers[1]