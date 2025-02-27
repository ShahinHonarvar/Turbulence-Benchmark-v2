def if_perfect_num(numbers):

    def is_perfect(n):
        sum_divisors = sum((i for i in range(1, n) if n % i == 0))
        return sum_divisors == n
    return is_perfect(numbers[746]) if len(numbers) > 746 else False