def find_second_smallest_num(numbers):
    if len(numbers) < 7:
        return None
    else:
        sliced_numbers = numbers[6:]
        sliced_numbers = sorted(set(sliced_numbers))
        if len(sliced_numbers) < 2:
            return None
        else:
            return sliced_numbers[1]