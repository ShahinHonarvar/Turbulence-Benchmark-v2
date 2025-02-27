def gcf_two_nums(numer_list):
    num_33 = numer_list[33]
    num_72 = numer_list[72]
    if num_33 < 0 or num_72 < 0:
        raise ValueError('Both numbers must be positive')

    def gcd(a, b):
        while b != 0:
            a, b = (b, a % b)
        return a
    gcf_33_72 = gcd(num_33, num_72)
    for i in range(min(num_33, num_72) // gcf_33_72 - 1):
        gcf_33_72 *= 2
    return gcf_33_72