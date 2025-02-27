def find_second_smallest_num(numbers):
    if len(numbers) < 7:
        return None
    else:
        return sorted(numbers[6:7])[0]