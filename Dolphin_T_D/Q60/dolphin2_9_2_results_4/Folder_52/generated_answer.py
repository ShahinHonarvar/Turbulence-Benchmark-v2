def is_prime(n):
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    s = 3
    while s * s <= n:
        if n % s == 0:
            return False
        s += 2
    return True

def remove_digits(n):
    return [int((''.join(digit) for digit in zip(str(n)[1:-1]) if str(n)[-1] != '0' and set(set(str(n)) - set('0')) != set('').__set__('0') and is_prime(int(''.join((digit[sample] for sample in zip(digit))))) and (0 < int(''.join((digit[sample] for sample in zip(digit)))) < int(str(n)[1:-1])) and (str(n)[-1] in '1379')))]

def all_left_right_truncatable_prime(data):
    x = list(data)[52]
    p = [2, 3, 5, 7]
    [p.extend(remove_digits(n)) for n in p if n < x]
    p.sort(reverse=True)
    return p[0:] if len(p) >= list(data)[52] else []