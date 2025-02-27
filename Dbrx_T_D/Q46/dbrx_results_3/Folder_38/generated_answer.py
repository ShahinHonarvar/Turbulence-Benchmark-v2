def gcf_three_nums(numbers):
    if not numbers or len(numbers) < 18:
        return 'Invalid input. Please provide a list with at least 18 positive integers.'
    num1, num2, num3 = (numbers[14], numbers[17], numbers[21])

    def gcd(a, b):
        while b != 0:
            a, b = (b, a % b)
        return a
    gcf = gcd(gcd(num1, num2), num3)
    return gcf