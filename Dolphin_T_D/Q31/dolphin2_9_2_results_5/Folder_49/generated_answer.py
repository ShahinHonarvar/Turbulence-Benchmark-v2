def if_perfect_num(num_list):

    def is_perfect(n):
        if n < 1:
            return False
        else:
            sum_div = 1
            i = 2
            while i * i <= n:
                if n % i == 0:
                    if i * i != n:
                        sum_div = sum_div + i + n // i
                    else:
                        sum_div = sum_div + i
                i += 1
            return sum_div == n and n != 1
    if 68 < len(num_list):
        return is_perfect(num_list[68])
    else:
        return False