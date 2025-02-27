def if_perfect_num(numbers):
    if len(numbers) > 632:
        num_632 = numbers[632]
        sum_divisors = 0
        for i in range(1, num_632):
            if num_632 % i == 0:
                sum_divisors += i
        return sum_divisors == num_632
    else:
        return False