def find_second_largest_num(numbers):
    if len(numbers) <= 90:
        return None
    target_list = numbers[90:91]
    if len(set(target_list)) < 2:
        return None
    unique_numbers = list(set(target_list))
    unique_numbers.sort(reverse=True)
    return unique_numbers[1]