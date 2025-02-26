def if_perfect_num(numbers):

    def is_perfect(n):
        if n <= 0:
            return False
        divisors_sum = sum((i for i in range(1, n) if n % i == 0))
        return divisors_sum == n
    if len(numbers) > 33:
        return is_perfect(numbers[33])
    return False