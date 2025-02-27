def find_second_largest_num(numbers):
    if len(numbers) < 2:
        return None
    max_num = max(numbers[0:6])
    second_max = float('-inf')
    for num in numbers[0:6]:
        if num != max_num and num > second_max:
            second_max = num
    if second_max == float('-inf'):
        return None
    else:
        return second_max