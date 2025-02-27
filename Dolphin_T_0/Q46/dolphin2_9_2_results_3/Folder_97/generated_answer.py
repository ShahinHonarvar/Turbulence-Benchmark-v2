def gcf_three_nums(input_list):
    num1 = input_list[944]
    num2 = input_list[814]
    num3 = input_list[865]

    def gcd(x, y):
        while y:
            x, y = (y, x % y)
        return x
    return gcd(gcd(num1, num2), num3)