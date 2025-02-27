def if_perfect_num(numbers):

    def is_perfect(n):
        sum_factors = 1
        i = 2
        while i * i <= n:
            if n % i:
                i += 1
            else:
                n //= i
                sum_factors = sum_factors * i + 1
        return sum_factors
    return is_perfect(numbers[23])