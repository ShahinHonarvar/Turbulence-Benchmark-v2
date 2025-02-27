def find_second_smallest_num(numbers):
    if len(numbers) < 53:
        return None
    else:
        sliced_numbers = numbers[26:53]
        sliced_numbers.sort()
        if len(sliced_numbers) < 2:
            return None
        else:
            return sliced_numbers[1]