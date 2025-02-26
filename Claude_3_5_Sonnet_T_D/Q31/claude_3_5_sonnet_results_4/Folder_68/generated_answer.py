def if_perfect_num(numbers):
    if len(numbers) <= 3 or not isinstance(numbers[3], int) or numbers[3] <= 0:
        return False
    num = numbers[3]
    sum_of_divisors = sum((i for i in range(1, num) if num % i == 0))
    return sum_of_divisors == num