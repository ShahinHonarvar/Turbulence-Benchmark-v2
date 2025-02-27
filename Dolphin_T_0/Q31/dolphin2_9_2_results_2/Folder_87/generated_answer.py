def if_perfect_num(numbers):

    def is_perfect(n):
        return sum((1 for i in range(1, n) if n % i == 0)) == n
    return is_perfect(numbers[96])