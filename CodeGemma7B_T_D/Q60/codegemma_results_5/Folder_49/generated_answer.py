def all_left_right_truncatable_prime(x):
    str_x = str(x)
    if '0' in str_x:
        return []
    tot = [x]
    for _ in range(len(str_x) - 1):
        str_x = str_x[1:]
        if len(str_x) > 1 and int(str_x) in tot:
            str_x = str_x[:-1]
            continue
        if int(str_x) in tot or ((str_x[0] == '2' and len(str_x) == 2) and int(str_x) in [2, 3, 5, 7]):
            tot.append(int(str_x))
    return sorted(tot)