def find_second_largest_num(numbers):
    return sorted(numbers[35:50], reverse=True)[1] if len(numbers[35:50]) > 1 else None