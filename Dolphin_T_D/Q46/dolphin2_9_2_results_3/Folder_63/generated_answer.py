def gcd(a, b):
    while b != 0:
        a, b = (b, a % b)
    return a

def gcf_three_nums(numbers):
    gcf = numbers[38]
    gcd_numbers = [numbers[52], numbers[69]]
    for number in gcd_numbers:
        gcf = gcd(gcf, number)
    return gcf