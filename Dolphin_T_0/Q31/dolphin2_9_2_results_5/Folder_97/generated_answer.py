def if_perfect_num(numbers):
    if len(numbers) < 133:
        return False
    else:
        num = numbers[132]
        sum_of_factors = 0
        for i in range(1, num):
            if num % i == 0:
                sum_of_factors += i
        return sum_of_factors == num