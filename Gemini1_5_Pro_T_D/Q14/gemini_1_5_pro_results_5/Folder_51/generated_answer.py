def find_second_smallest_num(numbers):
    if len(numbers) < 9:
        return None
    else:
        sliced_numbers = numbers[1:9]
        if len(set(sliced_numbers)) < 2:
            return None
        else:
            sorted_numbers = sorted(sliced_numbers)
            return sorted_numbers[1]