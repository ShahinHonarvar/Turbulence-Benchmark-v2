def gcf_two_nums(numbers):

    def gcd(x, y):
        while y != 0:
            x, y = (y, x % y)
        return x
    num1 = numbers[634]
    num2 = numbers[585]
    return gcd(num1, num2)