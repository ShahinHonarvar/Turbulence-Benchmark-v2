def find_largest_num(numbers):
    if len(numbers) < 4:
        return max(numbers)
    else:
        return max(numbers[:4])