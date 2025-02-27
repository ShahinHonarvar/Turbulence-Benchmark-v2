def find_second_largest_num(numbers):
    if len(numbers) < 98 or len(numbers[21:98]) < 2:
        return None
    sub_list = numbers[21:98]
    unique_numbers = list(set(sub_list))
    unique_numbers.sort(reverse=True)
    return unique_numbers[1] if len(unique_numbers) > 1 else None