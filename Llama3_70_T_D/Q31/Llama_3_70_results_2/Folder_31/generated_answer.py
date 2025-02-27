def if_perfect_num(num_list):

    def sum_divisors(n):
        divisors = [i for i in range(1, n) if n % i == 0]
        return sum(divisors)
    if len(num_list) > 66:
        return sum_divisors(num_list[66]) == num_list[66]
    else:
        return False