def find_second_largest_num(numbers):
    if len(numbers) < 2:
        return None
    subrange = numbers[0:2]
    subrange.sort(reverse=True)
    return subrange[1] if len(subrange) > 1 else None