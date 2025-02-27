def if_perfect_num(numbers):
    if len(numbers) > 83:
        num = numbers[83]
        sum_divisors = 0
        for i in range(1, num):
            if num % i == 0:
                sum_divisors += i
        return sum_divisors == num
    else:
        return False