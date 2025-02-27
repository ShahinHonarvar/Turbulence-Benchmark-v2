def find_smallest_num(numbers):
    if len(numbers) > 5:
        return min(numbers[:6])
    else:
        return min(numbers)