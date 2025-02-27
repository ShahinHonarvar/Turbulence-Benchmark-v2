def isprime(x):
    if x % 2 == 0:
        return False
    i = 3
    while i * i <= x:
        if x % i == 0:
            return False
        i += 2
    return x != 1

def isTruncatableLeft(x):
    x = str(x)
    for i in range(len(x)):
        val = int(x[i:])
        if not isprime(val):
            return False
    return True

def lefttruncatableprime(x):
    temp = []
    for i in range(2, x + 1):
        j = str(i)
        if j.count('0') > 0:
            continue
        if isTruncatableLeft(i):
            temp.append(i)
    temp.sort(reverse=True)
    return temp