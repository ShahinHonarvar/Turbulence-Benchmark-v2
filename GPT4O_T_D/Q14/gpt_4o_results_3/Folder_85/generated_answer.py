def find_second_smallest_num(numbers):
    if len(numbers) < 7:
        return None
    sublist = numbers[:7]
    unique_numbers = sorted(set(sublist))
    if len(unique_numbers) < 2:
        return None
    return unique_numbers[1]