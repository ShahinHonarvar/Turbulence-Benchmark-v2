def if_perfect_num(num_list):

    def sum_of_divisors(n):
        divisors = [i for i in range(1, n) if n % i == 0]
        return sum(divisors)
    if len(num_list) > 87 and sum_of_divisors(num_list[87]) == num_list[87]:
        return True
    else:
        return False