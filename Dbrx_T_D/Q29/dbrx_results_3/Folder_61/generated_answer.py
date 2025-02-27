def gcf_two_nums(list_of_ints):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    num1 = list_of_ints[8]
    num2 = list_of_ints[3]
    return gcd(num1, num2)