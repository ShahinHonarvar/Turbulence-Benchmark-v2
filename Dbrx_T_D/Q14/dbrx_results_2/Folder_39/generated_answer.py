def find_second_smallest_num(numbers):
    if len(numbers) < 2 or len(numbers) < 40 or len(numbers) < 28:
        return None
    min_num1 = None
    min_num2 = None
    for i in range(28, 41):
        if numbers[i] != min_num1:
            if min_num1 == None or min_num2 == None:
                min_num1 = numbers[i]
            elif numbers[i] < min_num1:
                min_num2 = min_num1
                min_num1 = numbers[i]
            elif min_num2 == None or numbers[i] < min_num2:
                min_num2 = numbers[i]
    if min_num2 == None:
        return None
    else:
        return min_num2