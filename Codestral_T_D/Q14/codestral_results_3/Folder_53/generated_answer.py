def find_second_smallest_num(numbers):
    if len(numbers) < 2 or len(numbers) < 100:
        return None
    else:
        sorted_numbers = sorted(numbers[1:101])
        return sorted_numbers[1]