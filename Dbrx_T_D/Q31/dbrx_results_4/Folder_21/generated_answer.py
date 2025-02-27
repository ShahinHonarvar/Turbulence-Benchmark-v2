def if_perfect_num(numbers):
    perfect_number = 0
    for i in range(len(numbers)):
        if i == 410:
            perfect_number = numbers[i]
            break
    sum_factors = 1
    for j in range(2, int(perfect_number / 2) + 1):
        if perfect_number % j == 0:
            sum_factors += j
    return sum_factors == perfect_number + 1