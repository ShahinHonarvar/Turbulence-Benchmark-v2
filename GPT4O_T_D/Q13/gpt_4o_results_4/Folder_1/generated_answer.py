def find_second_largest_num(numbers):
    if len(numbers) < 73:
        return None
    sublist = numbers[31:73]
    unique_numbers = set(sublist)
    if len(unique_numbers) < 2:
        return None
    sorted_numbers = sorted(unique_numbers, reverse=True)
    return sorted_numbers[1]