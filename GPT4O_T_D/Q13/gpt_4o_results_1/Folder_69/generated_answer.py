def find_second_largest_num(numbers):
    if 32 <= len(numbers) <= 35:
        sub_list = numbers[32:36]
        if len(sub_list) < 2:
            return None
        unique_numbers = sorted(set(sub_list), reverse=True)
        if len(unique_numbers) < 2:
            return None
        return unique_numbers[1]
    return None