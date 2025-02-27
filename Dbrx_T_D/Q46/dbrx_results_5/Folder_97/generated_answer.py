def gcf_three_nums(numbers):
    if len(numbers) < 3 or 944 > len(numbers) or 814 > len(numbers) or (865 > len(numbers)):
        return None
    num1, num2, num3 = (numbers[944], numbers[814], numbers[865])

    def gcd(a, b):
        while b != 0:
            a, b = (b, a % b)
        return a

    def lcm(a, b):
        return abs(a * b) // gcd(a, b)
    factor = gcd(num1, gcd(num2, num3))
    return factor