def if_perfect_num(num_list):
    n = num_list[828]
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