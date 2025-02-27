def gcf_two_nums(numbers):
    if not numbers or len(numbers) <= 95:
        return None
    num1 = numbers[87]
    num2 = numbers[95]

    def gcd(a, b):
        while b != 0:
            a, b = (b, a % b)
        return a

    def lcm(a, b):
        return a * b // gcd(a, b)
    return lcm(num1, num2)