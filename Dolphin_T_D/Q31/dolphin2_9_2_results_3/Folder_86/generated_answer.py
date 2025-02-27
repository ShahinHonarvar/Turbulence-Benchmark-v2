def if_perfect_num(num_list):

    def is_perfect(n):
        sum = 1
        i = 2
        while i * i <= n:
            if n % i == 0:
                if i * (n // i) == n:
                    sum += i
                else:
                    sum += i + n // i
            i += 1
        return sum == n
    return is_perfect(num_list[194])