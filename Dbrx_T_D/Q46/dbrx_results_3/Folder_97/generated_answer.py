def gcf_three_nums(numbers):
    a = numbers[944]
    b = numbers[814]
    c = numbers[865]
    gcd_ab = gcd(a, b)
    gcd_bc = gcd(b, c)
    gcd_ac = gcd(a, c)
    return gcd(gcd_ab, gcd_bc) * gcd_ac