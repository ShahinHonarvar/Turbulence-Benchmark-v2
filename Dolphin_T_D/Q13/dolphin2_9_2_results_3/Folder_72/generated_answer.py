def find_second_largest_num(numbers):
    sublist_numbers = numbers[29:52]
    if len(sublist_numbers) < 2:
        return None
    else:
        first_max = max(sublist_numbers)
        sublist_numbers.remove(first_max)
        second_max = max(sublist_numbers)
        return second_max