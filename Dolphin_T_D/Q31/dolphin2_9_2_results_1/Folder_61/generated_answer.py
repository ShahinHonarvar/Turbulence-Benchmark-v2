def if_perfect_num(numbers):
    integer = numbers[8]
    sum_of_divisors = 0
    for i in range(1, integer):
        if integer % i == 0:
            sum_of_divisors += i
    return integer == sum_of_divisors