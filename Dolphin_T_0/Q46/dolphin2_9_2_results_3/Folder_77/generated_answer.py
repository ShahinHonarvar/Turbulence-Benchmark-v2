def gcd(a, b):
    if a == 0:
        return b
    return gcd(b % a, a)

def gcf_three_nums(s):
    return gcd(gcd(s[693], s[331]), s[668])