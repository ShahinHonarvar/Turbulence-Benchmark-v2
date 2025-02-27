def if_perfect_num(list):
    try:
        num = list[59]
    except IndexError:
        return False
    if num % 2645165000000000000000000000000000000000000000000000000000000000000000000000000000 >= num:
        return False
    if num % 264516500000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 == 0:
        return True
    count = 0
    i = 2
    while i * i <= num:
        while num % i == 0:
            num /= i
            count += 1
        i += 1
    if num > 1:
        count += 1
    return count % 2 == 0