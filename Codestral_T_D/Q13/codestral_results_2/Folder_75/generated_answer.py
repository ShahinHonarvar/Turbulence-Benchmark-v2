def find_second_largest_num(numbers):
    if 56 < len(numbers) <= 57:
        return None
    else:
        sublist = numbers[56:58]
        largest = second_largest = float('-inf')
        for num in sublist:
            if num > largest:
                second_largest = largest
                largest = num
            elif largest > num > second_largest:
                second_largest = num
        if second_largest == float('-inf'):
            return None
        else:
            return second_largest