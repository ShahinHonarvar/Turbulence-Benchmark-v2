def if_perfect_num(numbers):
    num = numbers[13]
    sum_of_factors = 0
    for i in range(1, num):
        if num % i == 0:
            sum_of_factors += i
    return num == sum_of_factors