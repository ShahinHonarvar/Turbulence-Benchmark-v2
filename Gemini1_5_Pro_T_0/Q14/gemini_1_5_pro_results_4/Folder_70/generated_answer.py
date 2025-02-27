def find_second_smallest_num(numbers):
    if len(numbers) < 50:
        return None
    else:
        sliced_numbers = numbers[35:50]
        sorted_numbers = sorted(sliced_numbers)
        if len(sorted_numbers) >= 2:
            return sorted_numbers[1]
        else:
            return None