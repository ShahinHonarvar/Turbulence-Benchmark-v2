def find_second_largest_num(numbers):
    if len(numbers) == 0 or len(numbers) < 32:
        return None
    else:
        sublist = numbers[27:33]
        max_num = max(sublist)
        second_max = None
        for num in sublist:
            if num < max_num and (second_max is None or num > second_max):
                second_max = num
        return second_max