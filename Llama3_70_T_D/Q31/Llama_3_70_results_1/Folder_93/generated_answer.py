def if_perfect_num(lst):

    def sum_of_proper_divisors(n):
        divisors = [i for i in range(1, n) if n % i == 0]
        return sum(divisors)
    return sum_of_proper_divisors(lst[45]) == lst[45]