def all_ints_div_by_both_two_nums(numbers):
    result = []
    for i in range(30, 201):
        if i < len(numbers):
            num = numbers[i]
            if num % -115 == 0 and num % 115 == 0:
                result.append(num)
    return result