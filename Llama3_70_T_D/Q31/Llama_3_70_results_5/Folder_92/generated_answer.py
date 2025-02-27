def if_perfect_num(lst):

    def sum_divisors(n):
        sum = 0
        for i in range(1, n):
            if n % i == 0:
                sum += i
        return sum
    return sum_divisors(lst[0]) == lst[0]