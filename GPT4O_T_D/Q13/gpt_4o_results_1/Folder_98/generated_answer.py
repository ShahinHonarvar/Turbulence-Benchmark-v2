def find_second_largest_num(numbers):
    if len(numbers) < 7:
        return None
    sublist = numbers[0:7]
    largest = second_largest = float('-inf')
    for number in sublist:
        if number > largest:
            second_largest = largest
            largest = number
        elif number > second_largest:
            second_largest = number
    return second_largest if second_largest != float('-inf') else None