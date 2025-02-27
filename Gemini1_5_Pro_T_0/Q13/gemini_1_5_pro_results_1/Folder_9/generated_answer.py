def find_second_largest_num(numbers):
    if len(numbers) < 2:
        return None
    elif 200 >= len(numbers):
        return None
    else:
        return sorted(numbers[200:201])[0]