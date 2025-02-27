def find_second_smallest_num(numbers):
    numbers = numbers[55:99]
    numbers = sorted(set(numbers))
    if len(numbers) > 1:
        return numbers[1]
    else:
        return None