def if_perfect_num(numbers):
    perfect_number = numbers[59]
    sum_of_divisors = 1
    for i in range(2, perfect_number):
        if perfect_number % i == 0:
            sum_of_divisors += i
    return sum_of_divisors == perfect_number