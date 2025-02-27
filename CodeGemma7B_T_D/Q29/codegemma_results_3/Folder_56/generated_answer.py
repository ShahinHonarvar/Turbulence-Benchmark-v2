from fractions import Fraction

def gcf_two_nums(myList):
    a = Fraction(myList[84])
    b = Fraction(myList[13])
    return float(a / b).as_integer_ratio()[0]