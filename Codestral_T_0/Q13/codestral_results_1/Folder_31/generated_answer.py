def find_second_largest_num(numbers):
    sublist = numbers[75:89]
    if len(sublist) < 2:
        return None
    else:
        largest = second_largest = float('-inf')
        for num in sublist:
            if num > largest:
                second_largest = largest
                largest = num
            elif num > second_largest and num < largest:
                second_largest = num
        return second_largest if second_largest != float('-inf') else None