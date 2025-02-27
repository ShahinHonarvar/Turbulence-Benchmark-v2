def gcf_two_nums(numbers):
    num1 = numbers[47]
    num2 = numbers[97]

    def gcd(a, b):
        if a == 0:
            return b
        return gcd(b % a, a)
    return gcd(min(num1, num2), max(num1, num2))