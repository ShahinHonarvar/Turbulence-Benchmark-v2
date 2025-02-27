def find_second_smallest_num(numbers):
    if len(numbers) < 52:
        return None
    subarray = numbers[29:52]
    if len(set(subarray)) < 2:
        return None
    subarray.sort()
    return subarray[1]