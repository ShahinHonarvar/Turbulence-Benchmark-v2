def if_perfect_num(lst):
    num = lst[56]
    divisors = [1]
    for i in range(2, num):
        if num % i == 0:
            divisors.append(i)
    return sum(divisors) == num