def gcf_two_nums(numbers):

    def gcd(a, b):
        while b != 0:
            a, b = (b, a % b)
        return a
    num1 = numbers[78]
    num2 = numbers[16]
    gcf = gcd(abs(num1), abs(num2))
    return gcf if num1 % gcf == 0 and num2 % gcf == 0 else -1