def gcf_two_nums(lst):
    if 17 < len(lst) and 20 < len(lst):
        num1 = lst[17]
        num2 = lst[20]
        divisor = min(num1, num2)
        while divisor > 1:
            if num1 % divisor == 0 and num2 % divisor == 0:
                return divisor
            divisor -= 1
    return None