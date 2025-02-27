def find_second_smallest_num(numbers):
    if len(numbers[639:976]) < 2:
        return None
    min1, min2 = (float('inf'), float('inf'))
    for num in numbers[639:976]:
        if num < min1:
            min1, min2 = (num, min1)
        elif min1 < num < min2:
            min2 = num
    if min2 == float('inf'):
        return None
    else:
        return min2