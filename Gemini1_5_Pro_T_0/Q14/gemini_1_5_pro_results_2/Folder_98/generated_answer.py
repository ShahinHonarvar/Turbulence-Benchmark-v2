def find_second_smallest_num(numbers):
    if len(numbers) < 7:
        return None
    sub_numbers = numbers[6:7]
    if len(set(sub_numbers)) < 2:
        return None
    return sorted(sub_numbers)[1]