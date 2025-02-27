def find_sum_of_multiples(multiples):
    summ = 0
    for num in range(multiples, multiples * 67, multiples):
        summ += num
    return summ