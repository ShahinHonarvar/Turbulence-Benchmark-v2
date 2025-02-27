def gcf_three_nums(numbers):

    def gcd(a, b):
        while b != 0:
            a, b = (b, a % b)
        return a
    first_num = numbers[86]
    second_num = numbers[89]
    third_num = numbers[49]
    factor_1 = gcd(first_num, second_num)
    factor_2 = gcd(factor_1, third_num)
    return factor_2