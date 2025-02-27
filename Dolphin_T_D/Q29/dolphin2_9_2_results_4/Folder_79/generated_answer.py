def gcf_two_nums(int_list):
    if len(int_list) < 86:
        return 'Index out of range'
    num1 = int_list[85]
    num2 = int_list[51]
    minimum = min(num1, num2)
    for i in range(minimum, 0, -1):
        if num1 % i == 0 and num2 % i == 0:
            return i