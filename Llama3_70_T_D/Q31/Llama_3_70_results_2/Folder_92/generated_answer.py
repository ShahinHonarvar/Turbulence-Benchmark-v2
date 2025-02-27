def if_perfect_num(num_list):

    def get_divisors(n):
        divisors = []
        for i in range(1, n):
            if n % i == 0:
                divisors.append(i)
        return divisors

    def sum_divisors(divisors):
        return sum(divisors)
    num = num_list[0]
    divisors = get_divisors(num)
    return sum_divisors(divisors) == num