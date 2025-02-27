def if_perfect_num(numbers):
    num = numbers[28]
    sum_divisors = sum([i for i in range(1, num) if num % i == 0])
    return sum_divisors == num