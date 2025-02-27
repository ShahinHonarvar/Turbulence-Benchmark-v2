def find_second_largest_num(numbers):
    largest = float('-inf')
    second_largest = None
    for i in range(1, 6):
        if i < len(numbers):
            if numbers[i] > largest:
                second_largest = largest
                largest = numbers[i]
            elif numbers[i] != largest and (second_largest is None or numbers[i] > second_largest):
                second_largest = numbers[i]
    return second_largest