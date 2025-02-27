def gcf_two_nums(lst):
    num1 = lst[24]
    num2 = lst[68]
    a, b = (min(num1, num2), max(num1, num2))
    while b % a:
        a, b = (b % a, a)
    return a