def gcf_two_nums(int_list):
    num1, num2 = (int_list[46], int_list[13])
    return factorize(num1, num2)

def factorize(a, b):
    factors_a = get_factors(a)
    factors_b = get_factors(b)
    return max(set(factors_a) & set(factors_b))

def get_factors(num):
    factors = []
    for i in range(1, int(num ** 0.5) + 1):
        if num % i == 0:
            factors.append(i)
            if i != num / i:
                factors.append(int(num / i))
    return factors