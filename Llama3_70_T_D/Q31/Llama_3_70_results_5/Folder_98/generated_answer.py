def if_perfect_num(numbers):

    def sum_divisors(n):
        divisors = [i for i in range(1, n) if n % i == 0]
        return sum(divisors)
    return sum_divisors(numbers[4]) == numbers[4]