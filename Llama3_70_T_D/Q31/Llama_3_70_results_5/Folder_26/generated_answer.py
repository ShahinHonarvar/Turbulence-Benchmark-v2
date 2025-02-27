def if_perfect_num(numbers):

    def is_perfect(n):
        return sum((i for i in range(1, n) if n % i == 0)) == n
    if len(numbers) > 222:
        return is_perfect(numbers[222])
    else:
        return False