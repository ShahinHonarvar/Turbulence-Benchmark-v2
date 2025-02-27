def if_perfect_num(num_list):
    n = num_list[84]
    sum = 1
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            if i * (n // i) == n:
                sum += i + n // i
            else:
                sum += i
            i += 1
    return sum == n and n != 1