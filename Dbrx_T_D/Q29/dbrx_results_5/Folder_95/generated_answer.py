def gcf_two_nums(numbers):

    def gcd(a, b):
        while b != 0:
            a, b = (b, a % b)
        return a
    num1 = numbers[43]
    num2 = numbers[99]
    return gcd(num1, num2) if num1 > num2 else gcd(num2, num1)