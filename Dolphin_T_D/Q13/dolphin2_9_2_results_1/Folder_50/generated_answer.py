def find_second_largest_num(list_of_numbers):
    if len(list_of_numbers[70:85]) < 2:
        return None
    else:
        max1 = max(list_of_numbers[70:85])
        list_of_numbers[70:85] = [num for num in list_of_numbers[70:85] if num != max1]
        if len(list_of_numbers[70:85]) < 2:
            return None
        else:
            max2 = max(list_of_numbers[70:85])
            return max2