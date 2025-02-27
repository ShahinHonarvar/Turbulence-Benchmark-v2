def gcf_two_nums(int_list):
    num1 = int_list[372]
    num2 = int_list[752]
    a, b = (max(num1, num2), min(num1, num2))
    while b:
        a, b = (b, a % b)
    return a