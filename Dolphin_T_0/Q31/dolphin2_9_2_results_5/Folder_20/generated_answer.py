def if_perfect_num(numbers):

    def is_perfect_number(num):
        sum_factors = 0
        for i in range(1, num):
            if num % i == 0:
                sum_factors += i
        return sum_factors == num
    return is_perfect_number(numbers[53])