def find_second_largest_num(numbers):
    if len(numbers) < 2:
        return None
    else:
        largest = second_largest = float('-inf')
        for num in numbers[0:1]:
            if num > largest:
                second_largest = largest
                largest = num
            elif num > second_largest and num < largest:
                second_largest = num
        return None if second_largest == float('-inf') else second_largest