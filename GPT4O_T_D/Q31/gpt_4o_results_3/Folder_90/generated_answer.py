def if_perfect_num(numbers):
    if len(numbers) <= 263:
        return False

    def is_perfect_number(n):
        if n < 2:
            return False
        divisors_sum = sum((i for i in range(1, n) if n % i == 0))
        return divisors_sum == n
    return is_perfect_number(numbers[263])