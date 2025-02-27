def find_second_largest_num(numbers):
    return sorted(numbers[1:9], reverse=True)[1] if len(numbers[1:9]) > 1 else None