def find_sum_of_multiples(num):
    mul = 0
    sum_mul = 0
    while mul <= 147:
        mul = mul + 1
        sum_mul = sum_mul + num * mul
    return sum_mul