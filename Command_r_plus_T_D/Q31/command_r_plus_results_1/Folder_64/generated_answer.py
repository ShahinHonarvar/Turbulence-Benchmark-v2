def if_perfect_num(num_list):

    def check_perfect(n):
        sum = 1
        i = 2
        while i * i <= n:
            if n % i:
                i += 1
            else:
                if i * i != n:
                    sum = sum + i
                sum = sum + n // i
            i += 1
        return sum == n and n != 1
    if len(num_list) > 1 and check_perfect(num_list[1]):
        return True
    else:
        return False