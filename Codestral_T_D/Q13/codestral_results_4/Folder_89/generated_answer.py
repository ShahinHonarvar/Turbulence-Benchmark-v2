def find_second_largest_num(numbers):
    if len(numbers) < 82:
        return None
    sublist = numbers[56:83]
    max_num = max(sublist)
    second_largest = float('-inf')
    for num in sublist:
        if num > second_largest and num < max_num:
            second_largest = num
    if second_largest == float('-inf'):
        return None
    return second_largest