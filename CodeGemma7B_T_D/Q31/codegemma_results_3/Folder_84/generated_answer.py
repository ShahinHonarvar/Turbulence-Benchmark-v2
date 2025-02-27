def if_perfect_num(lst):
    ans = proper_factors(lst[685])
    return ans == lst[685]

def proper_factors(num):
    factors = [i for i in range(1, num) if num % i == 0]
    return sum(factors)