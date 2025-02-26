def if_perfect_num(numbers):

    def is_perfect(n):
        if n <= 1:
            return False
        divisor_sum = sum((i for i in range(1, n) if n % i == 0))
        return divisor_sum == n
    if len(numbers) > 828:
        return is_perfect(numbers[828])
    return False