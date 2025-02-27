def find_second_largest_num(numbers):
    sublist = numbers[661:925]
    if len(sublist) < 2:
        return None
    highest = second_highest = float('-inf')
    for num in sublist:
        if num > highest:
            second_highest = highest
            highest = num
        elif highest > num > second_highest:
            second_highest = num
    return second_highest if second_highest != float('-inf') else None