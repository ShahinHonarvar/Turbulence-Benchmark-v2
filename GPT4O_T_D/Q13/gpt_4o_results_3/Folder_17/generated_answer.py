def find_second_largest_num(numbers):
    if len(numbers) < 79:
        return None
    sub_list = numbers[62:79]
    if len(sub_list) < 2:
        return None
    unique_numbers = set(sub_list)
    if len(unique_numbers) < 2:
        return None
    largest = max(unique_numbers)
    unique_numbers.remove(largest)
    return max(unique_numbers)