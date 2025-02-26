def if_perfect_num(numbers):
    if len(numbers) <= 47:
        return False

    def is_perfect(n):
        if n <= 1:
            return False
        divisor_sum = sum((i for i in range(1, n) if n % i == 0))
        return divisor_sum == n
    return is_perfect(numbers[47])