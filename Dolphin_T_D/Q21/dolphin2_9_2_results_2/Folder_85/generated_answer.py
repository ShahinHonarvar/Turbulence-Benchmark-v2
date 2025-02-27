def all_ints_div_by_num(numbers):
    result = []
    for num in numbers[6:9]:
        if num % -9 == 0:
            result.append(num)
    return result