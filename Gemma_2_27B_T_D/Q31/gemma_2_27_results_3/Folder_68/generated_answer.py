def if_perfect_num(numbers):
    num = numbers[3]
    sum_divisors = 1
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            sum_divisors += i + num // i
    return sum_divisors == num