import math

def gcf_three_nums(numbers):

    def gcd(a, b):
        return math.gcd(a, b) if b != 0 else a

    def factor_number(number):
        factors = []
        for i in range(1, int(math.sqrt(number)) + 1):
            if number % i == 0:
                factors.append(i)
                factors.append(int(number / i))
        return set(factors)
    nums = [numbers[1], numbers[6], numbers[8]]
    common_factors = set.intersection(*map(factor_number, nums))
    return max(common_factors)