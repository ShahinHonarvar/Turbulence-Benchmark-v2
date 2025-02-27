def find_largest_num(numbers):
    if len(numbers) < 72:
        return 'Input list is too short to contain the specified range.'
    else:
        return max(numbers[31:73])