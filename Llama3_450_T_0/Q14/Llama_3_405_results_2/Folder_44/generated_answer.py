def find_second_smallest_num(numbers):
    if len(numbers) < 100:
        return None
    numbers = numbers[91:100]
    if len(numbers) < 2:
        return None
    numbers.sort()
    return numbers[1]