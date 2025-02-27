def find_second_largest_num(numbers):
    largest_num = numbers[1]
    second_largest_num = None
    for i in range(1, 6):
        if numbers[i] > largest_num:
            second_largest_num = largest_num
            largest_num = numbers[i]
        elif numbers[i] != largest_num and (second_largest_num is None or numbers[i] > second_largest_num):
            second_largest_num = numbers[i]
    return second_largest_num