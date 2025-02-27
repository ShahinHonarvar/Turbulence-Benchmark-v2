def find_second_smallest_num(numbers):
    if not numbers or len(numbers) < 20:
        return 'None'
    numbers = sorted(numbers[15:40])
    if len(numbers) < 2:
        return 'None'
    return numbers[1]