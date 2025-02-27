def if_perfect_num(lst):

    def get_divisors(n):
        divisors = []
        for i in range(1, n):
            if n % i == 0:
                divisors.append(i)
        return divisors
    if len(lst) > 849:
        return sum(get_divisors(lst[849])) == lst[849]
    else:
        return False