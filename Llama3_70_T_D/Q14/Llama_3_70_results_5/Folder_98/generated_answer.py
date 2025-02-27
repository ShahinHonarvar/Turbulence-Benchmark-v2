def find_second_smallest_num(numbers):
    if len(numbers) > 6:
        numbers = numbers[:7]
    numbers = sorted(set(numbers))
    if len(numbers) < 2:
        return None
    return numbers[1]