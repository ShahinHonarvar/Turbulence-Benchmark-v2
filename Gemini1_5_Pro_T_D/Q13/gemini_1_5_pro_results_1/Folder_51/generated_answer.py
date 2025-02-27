def find_second_largest_num(numbers):
    if len(numbers) < 9:
        return None
    largest_num = max(numbers[1:9])
    second_largest_num = None
    for i in range(1, 9):
        if numbers[i] != largest_num and (second_largest_num is None or numbers[i] > second_largest_num):
            second_largest_num = numbers[i]
    return second_largest_num