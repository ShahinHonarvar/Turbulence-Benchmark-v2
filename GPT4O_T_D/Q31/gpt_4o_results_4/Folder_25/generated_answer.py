def if_perfect_num(numbers):

    def is_perfect_number(n):
        return sum((i for i in range(1, n) if n % i == 0)) == n
    if len(numbers) > 90 and is_perfect_number(numbers[90]):
        return True
    return False