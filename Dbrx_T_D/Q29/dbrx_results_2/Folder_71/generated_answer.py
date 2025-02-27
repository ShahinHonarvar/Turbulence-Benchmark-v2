def gcf_two_nums(list_of_ints):

    def gcd(a, b):
        while b != 0:
            a, b = (b, a % b)
        return a
    num1 = list_of_ints[78]
    num2 = list_of_ints[93]
    return gcd(num1, num2)