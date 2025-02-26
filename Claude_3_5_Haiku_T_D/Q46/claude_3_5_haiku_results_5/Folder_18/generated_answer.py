def gcf_three_nums(numbers):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    a = numbers[637]
    b = numbers[411]
    c = numbers[757]
    result = gcd(a, gcd(b, c))
    return result