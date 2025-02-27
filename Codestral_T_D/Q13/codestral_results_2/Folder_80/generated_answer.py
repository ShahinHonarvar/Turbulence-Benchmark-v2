def find_second_largest_num(numbers):
    subset = numbers[64:67]
    largest = second_largest = float('-inf')
    for num in subset:
        if num > largest:
            second_largest = largest
            largest = num
        elif num > second_largest and num < largest:
            second_largest = num
    return second_largest if second_largest != float('-inf') else None