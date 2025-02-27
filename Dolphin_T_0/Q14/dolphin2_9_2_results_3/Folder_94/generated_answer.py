def find_second_smallest_num(list_numbers):
    if len(list_numbers[52:72]) < 2:
        return None
    else:
        return sorted(list_numbers[52:72])[1]