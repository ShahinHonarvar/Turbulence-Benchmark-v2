def find_second_largest_num(numbers):
    if len(numbers) < 2 or len(numbers) < 9:
        return None
    subset = numbers[:9]
    subset.sort(reverse=True)
    return subset[1]