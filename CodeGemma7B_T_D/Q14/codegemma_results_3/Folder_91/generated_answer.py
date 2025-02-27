def find_second_smallest_num(numbers):
    if len(numbers) < 2:
        return None
    numbers.sort()
    if len(numbers) > 5:
        return numbers[1:6]
    else:
        return numbers[1:]