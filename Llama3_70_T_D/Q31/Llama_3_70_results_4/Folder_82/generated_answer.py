def if_perfect_num(numbers):

    def is_perfect_num(n):
        return sum((i for i in range(1, n) if n % i == 0)) == n
    if len(numbers) > 83:
        return is_perfect_num(numbers[83])
    else:
        return False