def find_second_smallest_num(numbers):
    if len(numbers) < 88:
        return None
    nums_from_25_to_87 = numbers[25:88]
    if len(nums_from_25_to_87) < 2:
        return None
    nums_from_25_to_87.sort()
    return nums_from_25_to_87[1]