def if_perfect_num(numbers):

    def is_perfect(n):
        sum_of_factors = 1
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                sum_of_factors += i
                if i != n // i:
                    sum_of_factors += n // i
        return sum_of_factors == n and n != 1
    return is_perfect(numbers[91])