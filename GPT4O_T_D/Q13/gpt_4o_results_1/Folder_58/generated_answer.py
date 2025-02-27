def find_second_largest_num(numbers):
    if len(numbers) < 557:
        return None
    sublist = numbers[209:557]
    unique_sorted_numbers = sorted(set(sublist), reverse=True)
    return unique_sorted_numbers[1] if len(unique_sorted_numbers) > 1 else None