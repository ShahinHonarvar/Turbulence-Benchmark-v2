def if_perfect_num(numbers):

    def is_perfect(n):
        sum_divisors = sum([i for i in range(1, n) if n % i == 0])
        return sum_divisors == n
    if len(numbers) > 985 and is_perfect(numbers[985]):
        return True
    return False