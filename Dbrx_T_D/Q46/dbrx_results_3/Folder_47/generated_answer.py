def gcf_three_nums(numbers):
    gcf = lambda a, b: a if b == 0 else gcf(b, a % b)
    i = 36
    j = 85
    k = 83
    first_num = numbers[i]
    second_num = numbers[j]
    third_num = numbers[k]
    factor = 0
    for factor in range(min(first_num, second_num, third_num), 0, -1):
        if first_num % factor == 0 and second_num % factor == 0 and (third_num % factor == 0):
            break
    return factor