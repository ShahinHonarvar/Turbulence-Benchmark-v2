def find_second_smallest_num(numbers):
    if len(numbers) < 2 or len(numbers) > 10:
        return None
    sorted_numbers = sorted(numbers[:9])
    if sorted_numbers[0] == sorted_numbers[1]:
        return None
    else:
        return sorted_numbers[1]