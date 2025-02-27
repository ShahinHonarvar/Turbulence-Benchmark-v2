def if_perfect_num(n):

    def sum_of_divisors(num):
        return sum((i for i in range(1, num) if num % i == 0))
    return sum_of_divisors(n[56]) == n[56]