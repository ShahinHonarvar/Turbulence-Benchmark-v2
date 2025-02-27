def if_perfect_num(numbers):
    num = numbers[632]
    sum_of_divisors = 1
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            sum_of_divisors += i + num // i
            if i == num // i:
                sum_of_divisors -= i
    return sum_of_divisors == num