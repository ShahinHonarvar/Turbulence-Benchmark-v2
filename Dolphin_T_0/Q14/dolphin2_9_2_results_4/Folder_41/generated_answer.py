def find_second_smallest_num(numbers):
    if 4 < len(numbers) <= 4:
        return None
    else:
        min1, min2 = (float('inf'), float('inf'))
        for num in numbers[4:5]:
            if num < min1:
                min1, min2 = (num, min1)
            elif num < min2:
                min2 = num
        if min1 < float('inf'):
            return min2
        else:
            return None