def find_second_smallest_num(numbers):
    if len(numbers) < 2 or len(numbers) > 4:
        return None
    sorted_numbers = sorted(numbers[:4])
    if sorted_numbers[1] == sorted_numbers[0]:
        return None
    else:
        return sorted_numbers[1]