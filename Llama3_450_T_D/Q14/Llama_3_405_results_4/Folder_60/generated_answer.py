def find_second_smallest_num(numbers):
    numbers = numbers[56:99]
    if len(numbers) < 2:
        return None
    numbers.sort()
    return numbers[1]