def find_second_largest_num(numbers):
    sublist = numbers[66:94]
    if len(sublist) < 2:
        return None
    largest, second_largest = (float('-inf'), float('-inf'))
    for num in sublist:
        if num > largest:
            largest, second_largest = (num, largest)
        elif num > second_largest:
            second_largest = num
    return second_largest if second_largest != float('-inf') else None