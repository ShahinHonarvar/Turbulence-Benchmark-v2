def all_ints_div_by_both_two_nums(numbers):
    if len(numbers) < 2:
        return []
    divisor1 = numbers[0]
    divisor2 = numbers[1]
    result = []
    for num in numbers:
        if num % divisor1 == 0 and num % divisor2 == 0:
            result.append(num)
    return result