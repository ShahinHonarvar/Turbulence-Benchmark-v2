def find_second_largest_num(numbers):
    if len(numbers) < 92:
        return 'None'
    second_largest = sorted(numbers[19:93])[len(numbers[19:93]) - 2]
    return second_largest