def find_second_smallest_num(numbers):
    sub_numbers = numbers[36:52]
    sub_numbers = sorted(sub_numbers)
    if len(sub_numbers) < 2:
        return None
    return sub_numbers[1]