def gcf_two_nums(numbers):
    num1 = numbers[372]
    num2 = numbers[752]
    factors1 = list(set((i for i in range(1, num1 + 1) if num1 % i == 0)))
    factors2 = list(set((i for i in range(1, num2 + 1) if num2 % i == 0)))
    gcf_list = [i for i in factors1 if i in factors2]
    return max(gcf_list)