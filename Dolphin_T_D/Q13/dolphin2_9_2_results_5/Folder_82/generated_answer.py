def find_second_largest_num(numbers):
    subset = numbers[20:201] if 200 < len(numbers) else numbers[20:]
    if subset and len(set(subset)) >= 2:
        subset.sort()
        return subset[-2]
    else:
        return None