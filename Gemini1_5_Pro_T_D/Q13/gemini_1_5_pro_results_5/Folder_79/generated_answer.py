def find_second_largest_num(numbers):
    if len(numbers) < 5:
        return None
    else:
        sliced_numbers = numbers[4:5]
        if len(set(sliced_numbers)) < 2:
            return None
        else:
            return sorted(sliced_numbers)[-2]