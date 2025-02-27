def if_perfect_num(input_list):

    def is_perfect(n):
        if n < 6:
            return False
        sum_div = 1
        i = 2
        while i * i <= n:
            if n % i:
                i += 1
            else:
                if i * (n // i) == n:
                    sum_div = sum_div + i + n // i
                else:
                    sum_div = sum_div + i
                i += 1
        return sum_div == n
    return is_perfect(input_list[194])