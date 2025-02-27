def gcf_two_nums(numbers):

    def gcd(a, b):
        while b != 0:
            a, b = (b, a % b)
        return abs(a)
    num1 = numbers[224]
    num2 = numbers[663]
    if num1 == 0 or num2 == 0:
        raise ValueError('Both numbers must be non-zero.')
    return abs(gcd(num1, num2))