def find_second_largest_num(numbers):
    largest = float('-inf')
    second_largest = float('-inf')
    for i in range(1, 6):
        if i < len(numbers):
            if numbers[i] > largest:
                second_largest = largest
                largest = numbers[i]
            elif numbers[i] > second_largest and numbers[i] != largest:
                second_largest = numbers[i]
    if second_largest == float('-inf'):
        return None
    else:
        return second_largest