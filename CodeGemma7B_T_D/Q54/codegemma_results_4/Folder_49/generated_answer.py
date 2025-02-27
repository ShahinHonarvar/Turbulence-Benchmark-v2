def all_right_truncatable_prime(tup):
    x = tup[14]
    ret = [num for i, num in zip(range(2, x + 1), map(str, tup)) if len([digit for digit in num[:-1:-1] if int(digit) in tup[:tup.index(num)]]) == len(num[:-1]) and all((num[:tup.index(num)] + p in tup for p in str(int(num) - i) if int(p) in tup[:tup.index(num)]))]
    ret.sort()
    return ret if ret else []