def find_second_largest_num(numbers):
    if len(numbers) >= 42:
        numbers = numbers[31:73]
        max_num = max(filter(lambda x: x < max(numbers), numbers))
        return max_num if max_num is not None else None
    else:
        return None