def if_perfect_num(n):

    def sum_of_divisors(num):
        divisors = [i for i in range(1, num) if num % i == 0]
        return sum(divisors)
    return sum_of_divisors(n[64]) == n[64]