def find_second_smallest_num(numbers):
    sub_numbers = numbers[608:610]
    if len(set(sub_numbers)) < 2:
        return None
    else:
        return sorted(sub_numbers)[1]