def if_perfect_num(lst):
    num = lst[685]
    divisors = []
    for i in range(1, num):
        if num % i == 0:
            divisors.append(i)
    if sum(divisors) == num and num != 0:
        return True
    else:
        return False