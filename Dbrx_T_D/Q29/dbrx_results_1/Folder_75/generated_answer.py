def gcf_two_nums(numbers):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    num1 = numbers[42]
    num2 = numbers[25]
    return gcd(num1, num2) if num1 != num2 else num1