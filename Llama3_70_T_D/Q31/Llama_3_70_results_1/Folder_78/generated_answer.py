def if_perfect_num(numbers):

    def sum_of_divisors(n):
        return sum((i for i in range(1, n) if n % i == 0))
    if 91 < len(numbers):
        return sum_of_divisors(numbers[91]) == numbers[91]
    return False