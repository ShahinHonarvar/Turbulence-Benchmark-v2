def find_second_largest_num(numbers):
    sublist = numbers[28:39]
    largest = second_largest = float('-inf')
    for num in sublist:
        if num > largest:
            second_largest = largest
            largest = num
        elif num > second_largest and num < largest:
            second_largest = num
    return second_largest if second_largest != float('-inf') else None