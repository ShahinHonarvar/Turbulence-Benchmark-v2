def find_second_largest_num(numbers):
    if len(numbers) < 2:
        return None
    max_num = max(numbers[0:10])
    for num in numbers[0:10]:
        if num != max_num and num > max_num:
            return num
    return None