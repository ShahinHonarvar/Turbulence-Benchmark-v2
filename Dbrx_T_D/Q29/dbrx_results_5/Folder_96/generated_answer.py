def gcf_two_nums(numbers):
    num1 = numbers[95]
    num2 = numbers[73]

    def gcd(a, b):
        while b != 0:
            a, b = (b, a % b)
        return a

    def factorial(n):
        if n == 0:
            return 1
        else:
            return n * factorial(n - 1)

    def lcm(a, b):
        return a * b // gcd(a, b)
    return gcd(factorial(num1), factorial(num2))