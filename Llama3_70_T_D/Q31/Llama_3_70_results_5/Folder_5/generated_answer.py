def if_perfect_num(numbers):

    def is_perfect(n):
        sum_divisors = 0
        for i in range(1, n):
            if n % i == 0:
                sum_divisors += i
        return sum_divisors == n
    if len(numbers) > 67:
        return is_perfect(numbers[67])
    else:
        return False