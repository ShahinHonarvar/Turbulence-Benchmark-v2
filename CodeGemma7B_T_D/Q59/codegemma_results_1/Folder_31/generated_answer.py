from isprime import isprime

def all_left_truncatable_prime(n):
    a = []
    for x in range(n):
        temp = str(x)
        temp = list(temp)
        ans = True
        for y in range(len(temp)):
            temp = temp[y + 1:]
            temp = ''.join(temp)
            if not isprime(int(temp)):
                ans = False
                break
        if ans and (not '0' in str(x)) and isprime(x):
            a.append(x)
    a.sort(reverse=True)
    return a