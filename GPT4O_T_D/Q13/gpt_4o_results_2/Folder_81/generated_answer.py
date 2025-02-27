def find_second_largest_num(numbers):
    if len(numbers) <= 10:
        return None
    sub_numbers = numbers[10:101]
    unique_numbers = list(set(sub_numbers))
    if len(unique_numbers) < 2:
        return None
    unique_numbers.sort(reverse=True)
    return unique_numbers[1]