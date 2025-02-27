def if_perfect_num(numbers):
    index_93 = numbers[93]
    sum_of_factors = 0
    for i in range(1, index_93):
        if index_93 % i == 0:
            sum_of_factors += i
    if sum_of_factors == index_93:
        return True
    else:
        return False