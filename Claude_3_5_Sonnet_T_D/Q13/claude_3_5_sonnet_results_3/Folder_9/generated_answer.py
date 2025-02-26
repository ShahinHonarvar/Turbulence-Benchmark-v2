def find_second_largest_num(numbers):
    if len(numbers) < 201 or len(set(numbers[200:201])) < 2:
        return None
    return sorted(set(numbers[200:201]), reverse=True)[1]