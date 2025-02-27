def if_perfect_num(numbers):

    def sum_divisors(n):
        return sum((i for i in range(1, n) if n % i == 0))
    return sum_divisors(numbers[702]) == numbers[702]