def if_perfect_num(numbers):

    def is_perfect(n):
        sum_divisors = 0
        for i in range(1, int(n ** 0.5) + 1):
            if n % i == 0:
                if n / i == i:
                    sum_divisors += i
                else:
                    sum_divisors += i + n // i
        return sum_divisors == n
    return is_perfect(numbers[96])