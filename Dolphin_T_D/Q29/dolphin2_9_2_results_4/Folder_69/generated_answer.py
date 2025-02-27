def gcf_two_nums(l: list) -> int:
    num1 = l[894]
    num2 = l[801]
    for i in range(1, min(num1, num2) + 1):
        if num1 % i == 0 and num2 % i == 0:
            gcf = i
    return gcf