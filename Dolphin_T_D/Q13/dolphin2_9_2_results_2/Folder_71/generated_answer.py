def find_second_largest_num(numbers):
    sublist = numbers[26:52]
    max_num = max(sublist)
    second_max = None
    for num in sublist:
        if num < max_num and (second_max is None or num > second_max):
            second_max = num
    return second_max