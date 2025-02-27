def if_perfect_num(lst):
    if len(lst) > 132:
        num = lst[132]
        divisors_sum = sum([i for i in range(1, num) if num % i == 0])
        return True if divisors_sum == num else False
    else:
        return False