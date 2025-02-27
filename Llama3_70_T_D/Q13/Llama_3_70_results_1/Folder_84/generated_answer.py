def find_second_largest_num(numbers):
    if len(numbers) < 87:
        return None
    nums_slice = numbers[43:87]
    nums_slice.sort(reverse=True)
    if len(nums_slice) < 2:
        return None
    return nums_slice[1]