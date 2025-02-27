def find_second_largest_num(numbers):
    if len(numbers) < 73:
        return None
    sublist = numbers[31:73]
    if len(set(sublist)) < 2:
        return None
    largest = sublist[0]
    second_largest = sublist[0]
    for i in range(1, len(sublist)):
        if sublist[i] > largest:
            second_largest = largest
            largest = sublist[i]
        elif sublist[i] > second_largest and sublist[i] != largest:
            second_largest = sublist[i]
    return second_largest