def gcf_three_nums(numbers):
    a, b, c = (numbers[990], numbers[671], numbers[711])
    return gcd(a, gcd(b, c))

def gcd(x, y):
    while y:
        x, y = (y, x % y)
    return x