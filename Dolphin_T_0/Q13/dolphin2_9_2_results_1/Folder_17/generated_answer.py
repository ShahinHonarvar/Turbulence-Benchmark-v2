def find_second_largest_num(numbers):
    sublist = numbers[62:79]
    if len(sublist) < 2:
        return None
    else:
        first, second = (float('-inf'), float('-inf'))
        for num in sublist:
            if num > first:
                second = first
                first = num
            elif num > second and num != first:
                second = num
        if second != float('-inf'):
            return second
        else:
            return None