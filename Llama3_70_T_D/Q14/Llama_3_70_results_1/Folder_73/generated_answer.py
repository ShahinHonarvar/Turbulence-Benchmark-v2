def find_second_smallest_num(numbers):
    if 59 >= len(numbers) or 97 >= len(numbers):
        return None
    else:
        return sorted(numbers[59:98])[1]