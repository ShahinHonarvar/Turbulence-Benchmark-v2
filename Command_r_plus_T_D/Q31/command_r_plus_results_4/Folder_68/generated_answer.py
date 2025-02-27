def if_perfect_num(numbers_list):

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
    if len(numbers_list) > 3:
        return is_perfect(numbers_list[3])
    else:
        return False