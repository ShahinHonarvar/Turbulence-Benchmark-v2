def find_second_largest_num(numbers):
    if len(numbers) < 2:
        return None
    for i in range(34, 55):
        if i == 34:
            max1 = min1 = numbers[i]
        elif numbers[i] > max1:
            max1, min1 = (numbers[i], max1)
        elif numbers[i] < max1 and numbers[i] > min1:
            min1 = numbers[i]
    if max1 != min1:
        return min1
    else:
        return None