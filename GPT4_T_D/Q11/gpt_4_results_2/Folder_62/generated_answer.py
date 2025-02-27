def find_largest_num(numbers):
    if len(numbers) >= 100:
        return max(numbers[91:100])
    else:
        return 'The list doesnt contain at least 100 elements'