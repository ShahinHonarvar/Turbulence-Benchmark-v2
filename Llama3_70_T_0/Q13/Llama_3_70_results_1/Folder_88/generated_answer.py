def find_second_largest_num(numbers):
    if len(numbers) < 9:
        return None
    else:
        second_largest = float('-inf')
        largest = float('-inf')
        for num in numbers[4:9]:
            if num > largest:
                second_largest = largest
                largest = num
            elif num > second_largest and num != largest:
                second_largest = num
        if second_largest == float('-inf'):
            return None
        else:
            return second_largest