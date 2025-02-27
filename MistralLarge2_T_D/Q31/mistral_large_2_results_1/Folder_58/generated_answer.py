def is_perfect_number(n):
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

def if_perfect_num(lst):
    return is_perfect_number(lst[714])