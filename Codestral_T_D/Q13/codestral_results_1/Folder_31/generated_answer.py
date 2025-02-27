def find_second_largest_num(numbers):
    if 75 <= len(numbers) <= 88:
        relevant_numbers = numbers[75:89]
        largest = second_largest = float('-inf')
        for num in relevant_numbers:
            if num > largest:
                second_largest = largest
                largest = num
            elif num > second_largest and num < largest:
                second_largest = num
        return second_largest if second_largest != float('-inf') else None
    else:
        return None