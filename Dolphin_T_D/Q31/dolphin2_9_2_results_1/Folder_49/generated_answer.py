def if_perfect_num(list_of_numbers):
    num = list_of_numbers[68]
    sum_of_divisors = 0
    for i in range(1, num):
        if num % i == 0:
            sum_of_divisors += i
    return sum_of_divisors == num