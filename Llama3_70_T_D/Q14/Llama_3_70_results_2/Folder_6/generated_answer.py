def find_second_smallest_num(numbers):
    if len(numbers) < 80:
        return None
    nums_slice = sorted(numbers[29:80])
    if len(nums_slice) < 2:
        return None
    return nums_slice[1]