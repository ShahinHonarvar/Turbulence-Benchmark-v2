def gcf_three_nums(numbers):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    a = numbers[695]
    b = numbers[710]
    c = numbers[914]
    first_gcd = gcd(a, b)
    final_gcd = gcd(first_gcd, c)
    return final_gcd