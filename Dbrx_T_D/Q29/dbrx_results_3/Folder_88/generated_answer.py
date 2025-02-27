def gcf_two_nums(numbers):
    n1 = numbers[27]
    n2 = numbers[34]
    factor = 1
    for i in range(2, min(n1, n2) + 1):
        if n1 % i == 0 and n2 % i == 0:
            factor = i
    return factor