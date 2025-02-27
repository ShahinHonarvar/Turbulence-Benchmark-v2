def if_perfect_num(numbers):

    def is_perfect_num(n):
        sum_divisors = 0
        for i in range(1, n):
            if n % i == 0:
                sum_divisors += i
        return sum_divisors == n
    if len(numbers) > 19:
        return is_perfect_num(numbers[19])
    return False