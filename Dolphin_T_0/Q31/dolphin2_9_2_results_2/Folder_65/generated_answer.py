def if_perfect_num(numbers):
    index_35 = numbers[35]
    sum_of_divisors = 0
    for i in range(1, index_35):
        if index_35 % i == 0:
            sum_of_divisors += i
    if sum_of_divisors == index_35:
        return True
    else:
        return False