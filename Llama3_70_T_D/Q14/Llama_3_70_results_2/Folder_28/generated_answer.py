def find_second_smallest_num(numbers):
    numbers = numbers[22:51]
    numbers.sort()
    return numbers[1] if len(numbers) > 1 else None