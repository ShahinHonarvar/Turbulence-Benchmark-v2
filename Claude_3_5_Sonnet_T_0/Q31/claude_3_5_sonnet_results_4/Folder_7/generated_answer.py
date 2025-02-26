def if_perfect_num(numbers):
    if len(numbers) <= 851:
        return False
    num = numbers[851]
    sum_of_divisors = sum((i for i in range(1, num) if num % i == 0))
    return sum_of_divisors == num