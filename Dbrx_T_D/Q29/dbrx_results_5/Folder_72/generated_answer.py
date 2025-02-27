import math

def gcf_two_nums(lst):
    a = lst[18]
    b = lst[37]
    factors_a = []
    factors_b = []
    gcf = []
    for i in range(1, int(math.sqrt(a)) + 1):
        if a % i == 0:
            factors_a.append(i)
            if i * i != a and a / i != i:
                factors_a.append(int(a / i))
    for j in range(1, int(math.sqrt(b)) + 1):
        if b % j == 0:
            factors_b.append(j)
            if j * j != b and b / j != j:
                factors_b.append(int(b / j))
    gcf = [val for val in factors_a if val in factors_b]
    return max(gcf)