def find_second_largest_num(numbers):
    if len(numbers) < 67:
        return None
    sub_list = numbers[10:67]
    unique_numbers = list(set(sub_list))
    if len(unique_numbers) < 2:
        return None
    unique_numbers.sort(reverse=True)
    return unique_numbers[1]