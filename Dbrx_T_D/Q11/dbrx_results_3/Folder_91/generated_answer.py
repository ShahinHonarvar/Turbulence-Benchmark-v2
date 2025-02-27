def find_largest_num(numbers):
    if len(numbers) < 6:
        return max(numbers[:5])
    else:
        return max(numbers[:5] + numbers[5:])