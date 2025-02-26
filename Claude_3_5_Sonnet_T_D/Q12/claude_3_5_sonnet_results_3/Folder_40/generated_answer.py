def find_smallest_num(numbers):
    if len(numbers) >= 2:
        return min(numbers[0], numbers[1])
    elif len(numbers) == 1:
        return numbers[0]
    else:
        return None