def find_second_largest_num(numbers):
    if len(numbers) <= 1:
        return None
    max_num = numbers[0]
    second_max_num = None
    for i in range(6):
        if numbers[i] > max_num:
            second_max_num = max_num
            max_num = numbers[i]
        elif numbers[i] < max_num and (second_max_num is None or numbers[i] > second_max_num):
            second_max_num = numbers[i]
    return second_max_num