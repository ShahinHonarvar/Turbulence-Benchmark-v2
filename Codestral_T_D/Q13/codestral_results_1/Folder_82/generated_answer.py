def find_second_largest_num(numbers):
    sublist = numbers[20:201]
    if len(sublist) < 2:
        return None
    first_largest = max(sublist)
    second_largest = float('-inf')
    for num in sublist:
        if num > second_largest and num < first_largest:
            second_largest = num
    if second_largest == float('-inf'):
        return None
    return second_largest