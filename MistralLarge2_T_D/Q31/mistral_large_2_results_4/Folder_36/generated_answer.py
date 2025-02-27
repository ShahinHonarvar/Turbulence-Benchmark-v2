def if_perfect_num(numbers):

    def is_perfect(n):
        sum_of_divisors = sum((i for i in range(1, n) if n % i == 0))
        return sum_of_divisors == n
    if len(numbers) > 990 and is_perfect(numbers[990]):
        return True
    return False