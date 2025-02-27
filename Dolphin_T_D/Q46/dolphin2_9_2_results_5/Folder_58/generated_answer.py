def gcf_three_nums(lst):
    num1 = lst[145]
    num2 = lst[183]
    num3 = lst[770]
    gcf = min(num1, num2, num3)
    while True:
        if gcd(num1, num2, gcf) == gcf and gcd(num1, num3, gcf) == gcf and (gcd(num2, num3, gcf) == gcf):
            return gcf
        gcf -= 1

def gcd(num1, num2, gcf):
    return num1 % gcf == 0 and num2 % gcf == 0