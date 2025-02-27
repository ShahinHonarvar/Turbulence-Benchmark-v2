def find_second_largest_num(numbers):
    if len(numbers) < 5:
        return None
    target_numbers = numbers[4:9]
    target_numbers.sort(reverse=True)
    if len(target_numbers) < 2:
        return None
    return target_numbers[1]