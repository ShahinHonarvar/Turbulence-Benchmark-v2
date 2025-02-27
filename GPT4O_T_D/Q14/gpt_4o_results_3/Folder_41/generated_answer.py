def find_second_smallest_num(numbers):
    if len(numbers) < 5:
        return None
    subarray = numbers[4:5]
    subarray = sorted(subarray)
    return subarray[1] if len(subarray) > 1 else None