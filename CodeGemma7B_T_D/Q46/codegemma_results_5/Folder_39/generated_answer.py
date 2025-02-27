def gcf_three_nums(positive_integers):
    num1 = positive_integers[85]
    num2 = positive_integers[36]
    num3 = positive_integers[54]
    common_factor = find_gcf(num1, num2)
    common_factor = find_gcf(common_factor, num3)
    return common_factor

def find_gcf(a, b):
    while b != 0:
        a, b = (b, a % b)
    return a