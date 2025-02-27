def gcf_three_nums(numbers):
    a = numbers[944]
    b = numbers[814]
    c = numbers[865]
    gcd_elems = gcd(gcd(a, b), c)
    factors = [i for i in range(1, gcd_elems + 1) if gcd_elems % i == 0]
    return max(factors)

def gcd(a, b):
    while b != 0:
        a, b = (b, a % b)
    return a