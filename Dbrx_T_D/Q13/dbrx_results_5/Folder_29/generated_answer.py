def find_second_largest_num(numbers):
    if len(numbers) < 39:
        return None
    sublist = numbers[59:98]
    sorted_sublist = sorted(sublist, reverse=True)
    second_largest = sorted_sublist[1] if len(sorted_sublist) > 1 else None
    return second_largest