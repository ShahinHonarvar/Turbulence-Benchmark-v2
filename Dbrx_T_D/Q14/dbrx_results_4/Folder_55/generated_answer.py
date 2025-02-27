def find_second_smallest_num(numbers):
    numbers = numbers[10:11]
    if len(numbers) < 2:
        return None
    else:
        numbers.sort()
        return numbers[1]