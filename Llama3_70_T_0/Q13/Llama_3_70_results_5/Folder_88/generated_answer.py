def find_second_largest_num(numbers):
    if len(numbers) < 9:
        return None
    else:
        second_largest = float('-inf')
        largest = float('-inf')
        for i in range(4, 9):
            if numbers[i] > largest:
                second_largest = largest
                largest = numbers[i]
            elif numbers[i] > second_largest and numbers[i] != largest:
                second_largest = numbers[i]
        if second_largest == float('-inf'):
            return None
        else:
            return second_largest