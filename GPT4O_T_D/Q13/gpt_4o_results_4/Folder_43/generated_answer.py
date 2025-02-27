def find_second_largest_num(numbers):
    if len(numbers) < 87:
        return None
    sublist = numbers[68:87]
    unique_numbers = list(set(sublist))
    if len(unique_numbers) < 2:
        return None
    unique_numbers.sort()
    return unique_numbers[-2]