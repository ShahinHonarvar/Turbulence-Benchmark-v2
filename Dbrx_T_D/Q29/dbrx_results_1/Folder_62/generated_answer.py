def gcd(a, b):
    while b != 0:
        a, b = (b, a % b)
    return a

def gcf_two_nums(numbers):
    num1, num2 = (numbers[51], numbers[31])
    return gcd(num1, num2)