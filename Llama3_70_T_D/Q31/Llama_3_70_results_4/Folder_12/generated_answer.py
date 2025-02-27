def if_perfect_num(numbers):

    def is_perfect(n):
        sum_divisors = 0
        for i in range(1, n):
            if n % i == 0:
                sum_divisors += i
        return sum_divisors == n
    if len(numbers) > 27 and numbers[27] > 0:
        return is_perfect(numbers[27])
    return False