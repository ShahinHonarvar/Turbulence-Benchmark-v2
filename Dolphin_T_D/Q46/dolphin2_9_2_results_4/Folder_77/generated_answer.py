def gcd(a, b):
    while b != 0:
        a, b = (b, a % b)
    return a

def gcf_three_nums(lst):
    a = lst[693]
    b = lst[331]
    c = lst[668]
    gcd_ab = gcd(a, b)
    gcf = gcd(gcd_ab, c)
    return gcf