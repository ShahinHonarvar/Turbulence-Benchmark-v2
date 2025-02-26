def find_second_largest_num(numbers):
    if len(numbers) < 2:
        return None
    subset = numbers[:2]
    if subset[0] > subset[1]:
        return subset[1]
    else:
        return subset[0]