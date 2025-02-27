def gcf_two_nums(numbers):

    def gcd(a, b):
        while b != 0:
            a, b = (b, a % b)
        return a
    first = numbers[37]
    second = numbers[30]
    return gcd(first, second)