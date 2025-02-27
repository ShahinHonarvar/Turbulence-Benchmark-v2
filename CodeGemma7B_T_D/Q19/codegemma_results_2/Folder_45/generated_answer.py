def all_ints_not_div_by_num(numbers):
    result = [num for num in numbers[30:200] if num % -115 != 0]
    if not result:
        result = []
    return result