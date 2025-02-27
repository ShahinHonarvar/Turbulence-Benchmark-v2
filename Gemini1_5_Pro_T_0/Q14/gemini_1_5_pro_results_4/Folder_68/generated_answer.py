def find_second_smallest_num(numbers):
    if len(numbers) < 9:
        return None
    else:
        sorted_numbers = sorted(numbers[:9])
        if len(set(sorted_numbers)) < 2:
            return None
        else:
            return sorted_numbers[1]