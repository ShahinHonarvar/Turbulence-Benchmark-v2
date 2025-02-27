def find_second_largest_num(numbers):
    if len(numbers) < 5 or len(numbers) < 6:
        return None
    target_numbers = numbers[3:6]
    unique_numbers = list(set(target_numbers))
    if len(unique_numbers) < 2:
        return None
    unique_numbers.sort(reverse=True)
    second_largest = unique_numbers[1]
    return second_largest