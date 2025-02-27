def if_perfect_num(numbers):

    def is_perfect_num(n):
        if n < 1:
            return False
        return sum((is_divisible(n, i) for i in range(1, n))) == n

    def is_divisible(n1, n2):
        return n1 % n2 == 0
    if len(numbers) < 43:
        return False
    return is_perfect_num(numbers[42])