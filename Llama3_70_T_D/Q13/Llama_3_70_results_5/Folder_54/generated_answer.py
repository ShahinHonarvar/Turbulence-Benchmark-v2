def find_second_largest_num(numbers):
    second_largest = None
    for i in range(34, 56):
        if i < len(numbers):
            current_num = numbers[i]
            if second_largest == None or current_num > second_largest:
                second_largest = current_num
    return second_largest