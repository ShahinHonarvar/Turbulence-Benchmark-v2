def if_perfect_num(num_list):

    def is_perfect(n):
        sum = 1
        i = 2
        while i * i <= n:
            if n % i:
                i += 1
            else:
                if i * (n // i) == n:
                    sum = sum + i + n // i
                else:
                    sum += i
                i += 1
        return sum == n and n != 1
    if len(num_list) > 10 and is_perfect(num_list[10]):
        return True
    else:
        return False