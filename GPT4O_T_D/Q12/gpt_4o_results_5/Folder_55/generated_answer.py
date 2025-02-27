def find_smallest_num(numbers):
    if len(numbers) > 10:
        subset = numbers[:10]
    else:
        subset = numbers
    return min(subset)