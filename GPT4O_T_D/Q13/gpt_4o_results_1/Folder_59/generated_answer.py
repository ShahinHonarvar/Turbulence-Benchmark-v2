def find_second_largest_num(numbers):
    if len(numbers) < 10:
        return None
    sublist = numbers[:10]
    largest = second_largest = float('-inf')
    for num in sublist:
        if num > largest:
            second_largest = largest
            largest = num
        elif num > second_largest:
            second_largest = num
    return second_largest if second_largest != float('-inf') else None