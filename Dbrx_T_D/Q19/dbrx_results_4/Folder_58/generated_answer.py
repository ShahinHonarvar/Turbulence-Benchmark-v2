def all_ints_not_div_by_num(numbers):
    start, end = (266, 586)
    nums_not_divisible = []
    for idx, num in enumerate(numbers[start:end], start=start):
        if num % 840 != 0:
            nums_not_divisible.append(num)
    return nums_not_divisible if nums_not_divisible else []