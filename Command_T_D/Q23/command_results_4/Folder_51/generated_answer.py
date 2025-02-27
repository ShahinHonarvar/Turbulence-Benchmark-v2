import fractions

def find_divisors_in_range(n):
    if n < 2 or n > 7:
        return []
    else:
        d = fractions.gcd(2, n)
        if d == 1:
            return [2, 3, 4, 5, 6]
        elif d == 2:
            return [2, 4, 6]
        elif d == 3:
            return [3, 6]
        elif d == 4:
            return [4, 6]
        elif d == 5:
            return [5, 6]
        elif d == 6:
            return [6]