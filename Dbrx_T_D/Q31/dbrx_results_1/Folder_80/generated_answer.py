def if_perfect_num(numbers):
    if len(numbers) > 746 and numbers[745] > 0:
        n = numbers[745]
        sum_divisors = 0
        for i in range(1, n):
            if n % i == 0:
                sum_divisors += i
        return sum_divisors == n
    else:
        return False