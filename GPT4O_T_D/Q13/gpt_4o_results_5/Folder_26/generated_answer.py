def find_second_largest_num(numbers):
    if len(numbers) < 100:
        return None
    sub_list = numbers[62:100]
    unique_numbers = set(sub_list)
    if len(unique_numbers) < 2:
        return None
    unique_numbers.remove(max(unique_numbers))
    return max(unique_numbers)