def find_second_smallest_num(numbers):
    sub_numbers = numbers[19:93]
    if len(sub_numbers) < 2:
        return None
    elif len(set(sub_numbers)) < 2:
        return None
    else:
        sub_numbers.sort()
        return sub_numbers[1]