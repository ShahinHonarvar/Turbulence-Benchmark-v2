def if_perfect_num(numbers):

    def is_perfect(num):
        sum_factors = sum((i for i in range(1, num) if num % i == 0))
        return sum_factors == num
    if len(numbers) > 72:
        return is_perfect(numbers[72])
    return False