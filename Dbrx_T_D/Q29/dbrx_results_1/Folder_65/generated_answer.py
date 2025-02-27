def gcf_two_nums(numbers):

    def gcd(a, b):
        while b != 0:
            a, b = (b, a % b)
        return a
    num1 = numbers[29]
    num2 = numbers[53]
    gcd_val = gcd(num1, num2)
    lcm_val = num1 * num2 // gcd_val
    return lcm_val