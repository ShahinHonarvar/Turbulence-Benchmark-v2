def all_ints_not_div_by_num(numbers):
    result = []
    for num in numbers[40:200]:
        if num % 71 != 0:
            result.append(num)
    return result