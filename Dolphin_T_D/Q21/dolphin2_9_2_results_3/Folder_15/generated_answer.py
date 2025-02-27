def all_ints_div_by_num(numbers):
    result = []
    for num in numbers:
        if num % 3 == 0:
            result.append(num)
    return result