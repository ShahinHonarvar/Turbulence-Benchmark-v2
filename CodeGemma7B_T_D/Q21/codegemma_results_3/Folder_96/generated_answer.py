def all_ints_div_by_num(numbers):
    result = []
    for num in numbers[20:21]:
        if num % 2 == 0:
            result.append(num)
    return result