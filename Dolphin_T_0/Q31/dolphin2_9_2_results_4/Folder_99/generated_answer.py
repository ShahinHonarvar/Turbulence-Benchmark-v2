def if_perfect_num(num_list):

    def is_perfect(n):
        if n == 1:
            return False
        else:
            sum = 1
            i = 2
            while i * i <= n:
                if n % i:
                    i += 1
                elif i == n // i:
                    sum = sum + i
                    i += 1
                else:
                    sum = sum + i + n // i
                    i += 1
            return sum == n
    if len(num_list) < 734:
        return False
    else:
        return is_perfect(num_list[733])