def all_ints_div_by_num(numbers):
    divisible = []
    start, end = (29, 51)
    for num in numbers[start:end + 1]:
        if num % -37 == 0:
            divisible.append(num)
    return divisible