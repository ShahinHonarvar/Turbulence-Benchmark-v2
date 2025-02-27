def gcf_three_nums(numbers):
    if len(numbers) < 44:
        return None
    n1 = numbers[18]
    n2 = numbers[37]
    n3 = numbers[43]
    factors1 = [f for f in range(1, n1 + 1) if n1 % f == 0]
    factors2 = [f for f in range(1, n2 + 1) if n2 % f == 0]
    factors3 = [f for f in range(1, n3 + 1) if n3 % f == 0]
    common_factors = list(set(factors1).intersection(set(factors2)).intersection(set(factors3)))
    return max(common_factors)