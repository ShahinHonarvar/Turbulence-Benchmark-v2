def if_perfect_num(numbers):

    def sum_of_divisors(n):
        return sum((i for i in range(1, n) if n % i == 0))
    return sum_of_divisors(numbers[19]) == numbers[19]