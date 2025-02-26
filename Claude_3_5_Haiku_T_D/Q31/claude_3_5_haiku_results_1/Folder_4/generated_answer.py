def if_perfect_num(numbers):

    def is_perfect(n):
        if n <= 1:
            return False
        divisor_sum = sum((d for d in range(1, n) if n % d == 0))
        return divisor_sum == n
    if len(numbers) < 16:
        return False
    return is_perfect(numbers[15])