def if_perfect_num(numbers):

    def is_perfect_number(n):
        if n <= 1:
            return False
        divisors_sum = sum((i for i in range(1, n) if n % i == 0))
        return divisors_sum == n
    if len(numbers) > 15:
        return is_perfect_number(numbers[15])
    return False