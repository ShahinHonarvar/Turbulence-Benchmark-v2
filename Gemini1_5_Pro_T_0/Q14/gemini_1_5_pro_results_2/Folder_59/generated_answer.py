def find_second_smallest_num(numbers):
    if len(numbers) < 10:
        return None
    else:
        sorted_numbers = sorted(numbers[:10])
        return sorted_numbers[1]