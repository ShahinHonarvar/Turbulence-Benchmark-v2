import numpy as np

def gcf_three_nums(numbers):
    a, b, c = (numbers[15], numbers[51], numbers[76])
    arr = np.array([a, b, c])
    factors = []
    for num in arr:
        for i in range(1, num + 1):
            if num % i == 0:
                factors.append(i)
    common_factors = []
    for factor in factors:
        if factors.count(factor) == len(arr):
            common_factors.append(factor)
    return max(common_factors)