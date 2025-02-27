def if_perfect_num(numbers):
    if len(numbers) > 714:
        num = numbers[714]
        sum_of_divisors = sum((i for i in range(1, num) if num % i == 0))
        return sum_of_divisors == num
    return False