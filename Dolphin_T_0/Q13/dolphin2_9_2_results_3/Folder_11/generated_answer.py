def find_second_largest_num(numbers):
    if len(numbers) < 2:
        return None
    else:
        numbers = numbers[36:52]
        if len(numbers) < 2:
            return None
        else:
            max_num = max(numbers)
            numbers.remove(max_num)
            return max(numbers) if len(numbers) > 0 else None