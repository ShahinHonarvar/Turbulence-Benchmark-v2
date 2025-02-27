def find_second_largest_num(numbers):
    sublist = numbers[25:88]
    if len(sublist) < 2:
        return None
    largest = max(sublist[0], sublist[1])
    second_largest = min(sublist[0], sublist[1])
    for i in range(2, len(sublist)):
        if sublist[i] > largest:
            second_largest = largest
            largest = sublist[i]
        elif sublist[i] > second_largest and sublist[i] != largest:
            second_largest = sublist[i]
    return second_largest