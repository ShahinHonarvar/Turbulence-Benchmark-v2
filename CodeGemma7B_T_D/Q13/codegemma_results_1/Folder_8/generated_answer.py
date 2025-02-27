def find_second_largest_num(numbers):
    if len(numbers) - 2 < 23:
        return 'None'
    nums = sorted(numbers[23:24])
    return nums[-1]