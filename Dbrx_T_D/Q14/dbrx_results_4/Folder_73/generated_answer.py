def find_second_smallest_num(numbers):
    if len(numbers[59:98]) < 2:
        return None
    else:
        sorted_numbers = sorted(numbers[59:98])
        return sorted_numbers[1]