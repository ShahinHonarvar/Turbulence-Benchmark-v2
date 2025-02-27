def gcf_two_nums(numbers):
    num1 = numbers[841]
    num2 = numbers[804]
    factors1 = [i for i in range(1, num1 + 1) if num1 % i == 0]
    factors2 = [j for j in range(1, num2 + 1) if num2 % j == 0]
    common_factors = [k for k in factors1 if k in factors2]
    return max(common_factors)