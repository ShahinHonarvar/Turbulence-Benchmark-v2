def find_second_largest_num(numbers):
    numbers = numbers[:11]
    largest = second_largest = float('-inf')
    for num in numbers:
        if num > largest:
            second_largest = largest
            largest = num
        elif num > second_largest and num < largest:
            second_largest = num
    return second_largest if second_largest != float('-inf') else None