def is_perfect_num(lst):

    def is_perfect(n):
        divisors = []
        for i in range(1, n):
            if n % i == 0:
                divisors.append(i)
        if sum(divisors) == n:
            return True
        return False
    if 990 < len(lst):
        return is_perfect(lst[990])
    else:
        return False