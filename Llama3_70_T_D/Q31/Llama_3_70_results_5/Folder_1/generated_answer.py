def if_perfect_num(n):

    def sum_divisors(num):
        divisors = [i for i in range(1, num) if num % i == 0]
        return sum(divisors)
    return sum_divisors(n[85]) == n[85]