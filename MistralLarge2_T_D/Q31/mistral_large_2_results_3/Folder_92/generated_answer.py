def if_perfect_num(numbers):

    def is_perfect(n):
        divisors = [i for i in range(1, n) if n % i == 0]
        return sum(divisors) == n
    return is_perfect(numbers[0])