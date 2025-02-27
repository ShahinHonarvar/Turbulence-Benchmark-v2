def find_second_largest_num(numbers):
    if len(numbers) < 40:
        return None
    else:
        subset = numbers[35:50]
        unique_numbers = set(subset)
        if len(unique_numbers) < 2:
            return None
        else:
            sorted_unique_numbers = sorted(list(unique_numbers))
            return sorted_unique_numbers[-2]