import math

def find_divisors_in_range(n):
    if not isinstance(n, int) or n < 228 or n > 846:
        return []
    factors = []
    for i in range(2, int(math.ceil(math.sqrt(n)) + 1)):
        if n % i == 0:
            factors.append(i)
            while n % i == 0:
                n /= i
    if n > 1 and n not in factors:
        factors.append(n)
    if n + 1 not in factors:
        factors.append(n + 1)
    if n % 2 == 0 and n not in factors:
        factors.append(n / 2)
    if n % 3 == 0 and n not in factors:
        factors.append(n / 3)
    if n % 5 == 0 and n not in factors:
        factors.append(n / 5)
    if n % 7 == 0 and n not in factors:
        factors.append(n / 7)
    if n % 11 == 0 and n not in factors:
        factors.append(n / 11)
    if n % 13 == 0 and n not in factors:
        factors.append(n / 13)
    if n % 17 == 0 and n not in factors:
        factors.append(n / 17)
    if n % 19 == 0 and n not in factors:
        factors.append(n / 19)
    if n % 23 == 0 and n not in factors:
        factors.append(n / 23)
    if n % 29 == 0 and n not in factors:
        factors.append(n / 29)
    if n % 31 == 0 and n not in factors:
        factors.append(n / 31)
    if n % 37 == 0 and n not in factors:
        factors.append(n / 37)
    if n % 41 == 0 and n not in factors:
        factors.append(n / 41)
    if n % 43 == 0 and n not in factors:
        factors.append(n / 43)
    if n % 47 == 0 and n not in factors:
        factors.append(n / 47)
    if n % 53 == 0 and n not in factors:
        factors.append(n / 53)
    if n % 59 == 0 and n not in factors:
        factors.append(n / 59)
    if n % 61 == 0 and n not in factors:
        factors.append(n / 61)
    if n % 67 == 0 and n not in factors:
        factors.append(n / 67)
    if n % 71 == 0 and n not in factors:
        factors.append(n / 71)
    if n % 73 == 0 and n not in factors:
        factors.append(n / 73)
    if n % 79 == 0 and n not in factors:
        factors.append(n / 79)
    if n % 83 == 0 and n not in factors:
        factors.append(n / 83)
    if n % 89 == 0 and n not in factors:
        factors.append(n / 89)
    if n % 97 == 0 and n not in factors:
        factors.append(n / 97)
    if n % 101 == 0 and n not in factors:
        factors.append(n / 101)
    if n % 103 == 0 and n not in factors:
        factors.append(n / 103)
    if n % 107 == 0 and n not in factors:
        factors.append(n / 107)
    if n % 109 == 0 and n not in factors:
        factors.append(n / 109)
    if n % 113 == 0 and n not in factors:
        factors.append(n / 113)
    if n % 127 == 0 and n not in factors:
        factors.append(n / 127)
    if n % 131 == 0 and n not in factors:
        factors.append(n / 131)
    if n % 137 == 0 and n not in factors:
        factors.append(n / 137)
    if n % 139 == 0 and n not in factors:
        factors.append(n / 139)
    if n % 149 == 0 and n not in factors:
        factors.append(n / 149)
    if n % 151 == 0 and n not in factors:
        factors.append(n / 151)