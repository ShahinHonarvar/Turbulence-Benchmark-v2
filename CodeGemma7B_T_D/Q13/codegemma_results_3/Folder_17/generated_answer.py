def find_second_largest_num(numbers):
    if len(numbers) < 63 or len(numbers) > 79:
        return 'None'
    numbers.sort()
    return numbers[-2]