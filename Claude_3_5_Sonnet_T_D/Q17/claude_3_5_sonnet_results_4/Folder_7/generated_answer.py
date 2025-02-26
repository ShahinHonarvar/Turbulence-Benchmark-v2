def all_ints_div_by_both_two_nums(numbers):
    result = []
    for i in range(543, 585):
        if i < len(numbers):
            if numbers[i] % -553 == 0 and numbers[i] % -737 == 0:
                result.append(numbers[i])
    return result