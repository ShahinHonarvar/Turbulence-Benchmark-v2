def find_second_largest_num(numbers):
    if len(numbers) < 2 or len(numbers) - 32 < 2 or len(numbers) - 35 < 0:
        return None
    subset = numbers[32:36]
    subset.sort(reverse=True)
    if subset[0] == subset[1]:
        return None
    else:
        return subset[1]