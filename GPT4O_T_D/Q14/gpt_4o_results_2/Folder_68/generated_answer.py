def find_second_smallest_num(numbers):
    if len(numbers) >= 9:
        subset = numbers[:9]
        unique_numbers = list(set(subset))
        if len(unique_numbers) < 2:
            return None
        else:
            unique_numbers.sort()
            return unique_numbers[1]
    return None