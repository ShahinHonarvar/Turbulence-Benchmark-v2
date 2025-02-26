def find_second_largest_num(numbers):
    if len(numbers) <= 15:
        return None
    sublist = numbers[15:40]
    if len(sublist) < 2:
        return None
    largest = max(sublist)
    second_largest = float('-inf')
    for num in sublist:
        if num > second_largest and num < largest:
            second_largest = num
    return second_largest if second_largest != float('-inf') else None