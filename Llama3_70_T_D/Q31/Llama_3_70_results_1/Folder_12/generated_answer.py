def if_perfect_num(numbers):

    def sum_divisors(n):
        divisors = [i for i in range(1, n) if n % i == 0]
        return sum(divisors)
    if len(numbers) > 27 and sum_divisors(numbers[27]) == numbers[27]:
        return True
    return False