def gcf_two_nums(numbers):

    def gcd(a, b):
        while b != 0:
            a, b = (b, a % b)
        return abs(a)

    def lcm(a, b):
        return abs(a * b) // gcd(a, b) if a and b else 0
    num1 = numbers[49]
    num2 = numbers[53]
    gcf = 1
    for i in range(2, min(num1, num2) // 2 + 1):
        if num1 % i == 0 and num2 % i == 0:
            gcf = i
    return gcf