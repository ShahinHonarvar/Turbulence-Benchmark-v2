def if_perfect_num(num_list):

    def check_perfect(n):
        sum = 1
        i = 2
        while i * i <= n:
            if n % i:
                i += 1
            else:
                if i * (n // i) == n:
                    sum += i + n // i
                i += 1
        return sum == n and n != 1
    if len(num_list) > 72 and num_list[72] > 0:
        return check_perfect(num_list[72])
    else:
        return False