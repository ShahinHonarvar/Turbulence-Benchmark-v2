def all_left_truncatable_prime(tup):
    num = str(tup[429])
    res = []
    for digit in range(1, int(num) + 1):
        str_digit = str(digit)
        local_num = num
        if '0' in str_digit:
            continue
        while len(local_num) > 0:
            if int(local_num) in [2, 3, 5, 7]:
                local_num = local_num[1:]
                if len(local_num) > 0:
                    continue
            else:
                break
        if len(local_num) == 0:
            res.append(digit)
    return sorted(res, reverse=True)