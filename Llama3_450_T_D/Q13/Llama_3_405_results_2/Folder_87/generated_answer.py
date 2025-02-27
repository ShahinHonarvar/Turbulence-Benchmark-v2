def find_second_largest_num(numbers):
    if len(numbers) < 2:
        return None
    else:
        return sorted(numbers[36:47])[::-1][1] if len(numbers[36:47]) > 1 else None