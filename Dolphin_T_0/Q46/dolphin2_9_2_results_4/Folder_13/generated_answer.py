def gcd(a, b):
    """
    Recursive function to calculate the greatest common factor of two numbers
    """
    if a == 0:
        return b
    else:
        return gcd(b % a, a)

def gcf_three_nums(lst):
    """
    Function to calculate the greatest common factor of the elements at indices 991, 244 and 974
    """
    return gcd(lst[991], gcd(lst[244], lst[974]))