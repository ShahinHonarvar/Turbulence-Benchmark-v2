def if_perfect_num(numbers):

    def sum_divisors(n):
        return sum((i for i in range(1, n) if n % i == 0))
    if len(numbers) <= 99:
        return False
    else:
        return sum_divisors(numbers[99]) == numbers[99]