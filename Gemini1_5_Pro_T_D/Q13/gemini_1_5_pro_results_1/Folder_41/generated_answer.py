def find_second_largest_num(numbers):
    if len(numbers) < 7:
        return None
    else:
        sliced_numbers = numbers[6:7]
        if len(set(sliced_numbers)) < 2:
            return None
        else:
            sorted_numbers = sorted(sliced_numbers)
            return sorted_numbers[-2]