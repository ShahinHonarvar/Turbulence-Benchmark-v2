def find_second_largest_num(numbers):
    if 200 < len(numbers) < 40:
        return None
    else:
        sublist = numbers[40:201]
        unique_numbers = list(set(sublist))
        if len(unique_numbers) < 2:
            return None
        unique_numbers.sort()
        return unique_numbers[1]