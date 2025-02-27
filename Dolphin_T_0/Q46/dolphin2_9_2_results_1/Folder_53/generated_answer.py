def gcf_three_nums(list_of_ints):
    num1 = list_of_ints[66]
    num2 = list_of_ints[56]
    num3 = list_of_ints[92]

    def gcd(a, b):
        if b == 0:
            return a
        else:
            return gcd(b, a % b)
    return gcd(gcd(num1, num2), num3)