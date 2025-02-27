def find_second_largest_num(numbers):
    if len(numbers) < 5:
        return None
    subset = numbers[1:6]
    subset.sort()
    if subset[-2] is None:
        return None
    index = subset.index(subset[-2])
    return numbers[index + 1]