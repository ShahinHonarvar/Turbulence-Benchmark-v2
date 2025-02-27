def if_perfect_num(numbers):
    if len(numbers) <= 849:
        return False

    def is_perfect_number(n):
        divisors_sum = sum((i for i in range(1, n) if n % i == 0))
        return divisors_sum == n
    return is_perfect_number(numbers[849])