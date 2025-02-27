def find_second_smallest_num(numbers):
    if len(numbers) < 42:
        return None
    numbers = numbers[31:73]
    numbers.sort()
    if len(numbers) >= 2:
        return numbers[1]
    else:
        return None