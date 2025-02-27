def if_perfect_num(numbers):

    def is_perfect_number(n):
        sum_of_divisors = sum((i for i in range(1, n) if n % i == 0))
        return sum_of_divisors == n
    if len(numbers) > 132:
        return is_perfect_number(numbers[132])
    return False