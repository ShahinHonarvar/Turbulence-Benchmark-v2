def if_perfect_num(lst):
    perfect_num = lst[746]
    divisors = [1]
    for i in range(2, perfect_num):
        if perfect_num % i == 0:
            divisors.append(i)
    return sum(divisors) == perfect_num