def find_smallest_num(numbers):
    if len(numbers) >= 6:
        return min(numbers[:6])
    else:
        return 'The list does not contain enough elements.'