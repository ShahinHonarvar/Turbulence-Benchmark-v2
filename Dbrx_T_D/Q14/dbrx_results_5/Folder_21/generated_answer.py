def find_second_smallest_num(numbers):
    if len(numbers) < 2 or len(numbers) < 925:
        return None
    min_num = min(numbers[660:925])
    second_num = None
    for num in numbers[660:925]:
        if num > min_num:
            if second_num is None or num < second_num:
                second_num = num
    if second_num == None:
        return None
    else:
        return second_num