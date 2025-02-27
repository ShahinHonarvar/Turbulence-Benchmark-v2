def if_perfect_num(numbers):

    def is_perfect(n):
        sum_divisors = 0
        for i in range(1, n):
            if n % i == 0:
                sum_divisors += i
        return sum_divisors == n
    if len(numbers) > 828 and numbers[828] > 0:
        return is_perfect(numbers[828])
    else:
        return False