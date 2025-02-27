def find_second_largest_num(numbers):
    sublist = numbers[4:5]
    if len(sublist) < 2:
        return None
    largest = second_largest = float('-inf')
    for n in sublist:
        if n > largest:
            second_largest = largest
            largest = n
        elif n > second_largest and n < largest:
            second_largest = n
    return second_largest if second_largest != float('-inf') else None