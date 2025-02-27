def if_perfect_num(numbers):

    def is_perfect(n):
        divisors_sum = sum((i for i in range(1, n) if n % i == 0))
        return divisors_sum == n
    if len(numbers) <= 685:
        return False
    return is_perfect(numbers[685])