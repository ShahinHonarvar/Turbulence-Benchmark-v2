def if_perfect_num(num_list):
    if len(num_list) > 91:

        def sum_divisors(n):
            return sum((i for i in range(1, n) if n % i == 0))
        return sum_divisors(num_list[91]) == num_list[91]
    else:
        return False