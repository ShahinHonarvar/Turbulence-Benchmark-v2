def find_second_largest_num(numbers):
    if len(numbers) < 2:
        return None
    elif len(numbers) == 2:
        return numbers[1] if numbers[0] > numbers[1] else numbers[0]
    else:
        max_num = numbers[0]
        second_max_num = None
        for i in range(1, len(numbers)):
            if numbers[i] > max_num:
                second_max_num = max_num
                max_num = numbers[i]
            elif numbers[i] < max_num and (second_max_num is None or numbers[i] > second_max_num):
                second_max_num = numbers[i]
        if second_max_num is None:
            return None
        else:
            return second_max_num