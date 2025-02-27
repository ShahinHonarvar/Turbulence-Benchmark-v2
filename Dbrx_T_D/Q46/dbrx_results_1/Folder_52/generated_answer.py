def gcf_three_nums(numbers):
    if len(numbers) < 75:
        return 'The list must have at least 75 elements.'
    a, b, c = (numbers[18], numbers[48], numbers[73])

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a

    def lcm(a, b):
        return a * b // gcd(a, b)
    result = gcd(gcd(a, b), c)
    return lcm(lcm(a, b), c) // result