def if_perfect_num(numbers):

    def is_perfect(n):
        if n < 1:
            return False
        sum_divisors = 0
        for i in range(1, n):
            if n % i == 0:
                sum_divisors += i
        return sum_divisors == n
    if 247 < len(numbers):
        return is_perfect(numbers[247])
    else:
        return False