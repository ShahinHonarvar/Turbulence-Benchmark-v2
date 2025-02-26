def find_second_largest_num(numbers):
    if len(numbers) <= 10 or len(numbers) < 101:
        return None
    sublist = numbers[10:101]
    if len(sublist) < 2:
        return None
    first_largest = max(sublist)
    second_largest = float('-inf')
    for num in sublist:
        if num > second_largest and num < first_largest:
            second_largest = num
    return second_largest if second_largest != float('-inf') else None