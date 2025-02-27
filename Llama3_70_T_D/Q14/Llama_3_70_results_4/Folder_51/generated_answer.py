def find_second_smallest_num(numbers):
    numbers = numbers[1:9]
    numbers = sorted(set(numbers))
    return numbers[1] if len(numbers) > 1 else None