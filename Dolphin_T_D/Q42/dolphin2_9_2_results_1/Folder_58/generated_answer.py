def gcd(x, y):
    while y:
        x, y = (y, x % y)
    return x

def prime_factors(arr):
    gcd_value = arr[0]
    for i in range(1, len(arr)):
        gcd_value = gcd(arr[i], gcd_value)
    prime_factor_set = set()
    for i in range(2, gcd_value + 1):
        if gcd_value % i == 0:
            if i % 2 != 0 and i % 3 != 0 and (i % 5 != 0) and (i % 7 != 0):
                prime_factor_set.add(i)
            elif i % 2 == 0 and i % 3 != 0 and (i % 5 != 0) and (i % 7 != 0):
                prime_factor_set.add(2)
            elif i % 3 == 0 and i % 2 != 0 and (i % 5 != 0) and (i % 7 != 0):
                prime_factor_set.add(3)
            elif i % 5 == 0 and i % 2 != 0 and (i % 3 != 0) and (i % 7 != 0):
                prime_factor_set.add(5)
            elif i % 7 == 0 and i % 2 != 0 and (i % 3 != 0) and (i % 5 != 0):
                prime_factor_set.add(7)
    return prime_factor_set