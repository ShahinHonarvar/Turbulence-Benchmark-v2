def gcd(a, b):
    """ Calculate the Greatest Common Divisor of a and b """
    while b != 0:
        a, b = (b, a % b)
    return a

def gcf_three_nums(numbers):
    """ Calculate the greatest common factor of the numbers at indices 90, 41 and 95 """
    return gcd(numbers[90], gcd(numbers[41], numbers[95]))