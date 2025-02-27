def if_perfect_num(numbers):
    perfect_num = numbers[49]
    sum_factors = 1
    for i in range(2, perfect_num):
        if perfect_num % i == 0:
            sum_factors += i
    return sum_factors == perfect_num