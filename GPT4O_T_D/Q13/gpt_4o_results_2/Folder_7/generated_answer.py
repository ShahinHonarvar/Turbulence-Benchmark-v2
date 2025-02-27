def find_second_largest_num(numbers):
    if len(numbers) < 925:
        return None
    subarray = numbers[661:925]
    unique_sorted = sorted(set(subarray))
    if len(unique_sorted) < 2:
        return None
    return unique_sorted[-2]