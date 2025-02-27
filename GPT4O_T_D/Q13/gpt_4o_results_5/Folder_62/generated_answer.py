def find_second_largest_num(numbers):
    if len(numbers) < 100:
        return None
    sub_list = numbers[91:100]
    unique_numbers = list(set(sub_list))
    if len(unique_numbers) < 2:
        return None
    unique_numbers.sort(reverse=True)
    return unique_numbers[1]