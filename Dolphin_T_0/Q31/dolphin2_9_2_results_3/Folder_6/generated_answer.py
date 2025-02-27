def if_perfect_num(lst):
    num = lst[790]
    divisors = [1]
    for i in range(2, num // 2 + 1):
        if num % i == 0:
            divisors.append(i)
    return sum(divisors) == num