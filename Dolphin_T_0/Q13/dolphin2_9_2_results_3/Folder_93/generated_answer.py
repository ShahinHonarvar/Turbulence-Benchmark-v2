def find_second_largest_num(numbers):
    sublist = numbers[74:95]
    if sublist:
        unique_numbers = list(set(sublist))
        sorted_numbers = sorted(unique_numbers)
        if len(sorted_numbers) > 1:
            return sorted_numbers[-2]
    return None