def if_perfect_num(numbers):
    perfect_num = numbers[27]
    sum_divisors = 0
    for i in range(1, perfect_num):
        if perfect_num % i == 0:
            sum_divisors += i
    if sum_divisors == perfect_num and perfect_num != 0:
        return True
    else:
        return False