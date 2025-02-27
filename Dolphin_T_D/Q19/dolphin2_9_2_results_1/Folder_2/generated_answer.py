def all_ints_not_div_by_num(numbers):
    result = []
    for num in numbers[21:50]:
        if num % 40 != 0:
            result.append(num)
    return result