def is_prime(n):
    if n in (0, 1):
        return False
    fs = factors(n) if n > 1 else [1]
    if len(fs) == 1:
        return True
    return False

def factors(n):
    i = 2
    fs = []
    while i * i <= n:
        if n % i:
            if n % (i + 2) != 0:
                i += 1
            else:
                fs.append(i + 2)
                n = n / (i + 2)
        else:
            fs.append(i)
            n = n / i
    if n > 1:
        fs.append(n)
    return fs

def all_left_right_truncatable_prime(x):
    l = []
    for i in range(2, x + 1):
        s = str(i)
        if s.count('0') == 0:
            while len(s) > 1:
                if is_prime(int(s)):
                    if len(s) == 2 or s.startswith('1') == 0:
                        s = s[1:-1]
                        if len(s) > 0 and is_prime(int(s)):
                            l.append(i)
                            break
                else:
                    break
    l.sort(reverse=True)
    return l