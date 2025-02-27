def if_perfect_num(numbers):

    def is_perfect(n):
        divisors = [i for i in range(1, n) if n % i == 0]
        return sum(divisors) == n
    if len(numbers) > 312 and numbers[312] > 0:
        return is_perfect(numbers[312])
    return False