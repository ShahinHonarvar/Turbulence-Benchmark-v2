def if_perfect_num(list_of_ints):

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
                    sum = sum + i
                i += 1
        return sum == n and n != 1
    if len(list_of_ints) >= 73:
        return is_perfect(list_of_ints[72])
    else:
        return False