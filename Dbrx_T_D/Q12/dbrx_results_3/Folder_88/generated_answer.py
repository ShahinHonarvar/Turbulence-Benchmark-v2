def find_smallest_num(numbers):
    if len(numbers) < 9:
        return 'Input list should contain at least 9 elements.'
    else:
        sublist = numbers[6:9]
        return min(sublist)