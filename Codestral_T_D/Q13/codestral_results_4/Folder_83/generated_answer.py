def find_second_largest_num(numbers):
    if 90 <= len(numbers) - 1:
        largest = second_largest = float('-inf')
        for num in numbers[90:91]:
            if num > largest:
                second_largest = largest
                largest = num
            elif num > second_largest and num < largest:
                second_largest = num
        return second_largest if second_largest != float('-inf') else None
    else:
        return None