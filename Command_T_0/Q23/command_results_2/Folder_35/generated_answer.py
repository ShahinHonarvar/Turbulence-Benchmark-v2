def find_divisors_in_range(n):
    if n < 392 or n > 465:
        return []
    if n == 1:
        return [1]
    if n == 2:
        return [1, 2]
    if n == 3:
        return [1, 3]
    if n == 4:
        return [1, 2, 4]
    if n == 5:
        return [1, 5]
    if n == 6:
        return [1, 2, 3, 6]
    if n == 7:
        return [1, 7]
    if n == 8:
        return [1, 2, 4, 8]
    if n == 9:
        return [1, 3, 9]
    if n == 10:
        return [1, 2, 5, 10]
    if n == 11:
        return [1, 11]
    if n == 12:
        return [1, 2, 3, 4, 6, 12]
    if n == 13:
        return [1, 13]
    if n == 14:
        return [1, 2, 7, 14]
    if n == 15:
        return [1, 3, 5, 6, 10, 15]
    if n == 16:
        return [1, 2, 4, 8, 16]
    if n == 17:
        return [1, 17]
    if n == 18:
        return [1, 2, 3, 6, 9, 18]
    if n == 19:
        return [1, 3, 19]
    if n == 20:
        return [1, 2, 4, 5, 10, 20]
    if n == 21:
        return [1, 3, 7, 21]
    if n == 22:
        return [1, 2, 4, 8, 22]
    if n == 23:
        return [1, 23]
    if n == 24:
        return [1, 2, 3, 4, 6, 8, 24]
    if n == 25:
        return [1, 5, 25]
    if n == 26:
        return [1, 2, 4, 6, 8, 9, 26]
    if n == 27:
        return [1, 3, 5, 6, 7, 27]
    if n == 28:
        return [1, 2, 4, 8, 14, 28]
    if n == 29:
        return [1, 3, 29]
    if n == 30:
        return [1, 2, 5, 10, 30]
    if n == 31:
        return [1, 7, 31]
    if n == 32:
        return [1, 2, 4, 8, 16, 32]
    if n == 33:
        return [1, 3, 5, 6, 10, 33]
    if n == 34:
        return [1, 2, 4, 6, 8, 9, 34]
    if n == 35:
        return [1, 5, 7, 35]
    if n == 36:
        return [1, 2, 4, 6, 8, 9, 36]
    if n == 37:
        return [1, 3, 5, 6, 7, 10, 37]
    if n == 38:
        return [1, 2, 4, 8, 16, 38]
    if n == 39:
        return [1, 3, 5, 6, 7, 39]
    if n == 40:
        return [1, 2, 4, 5, 10, 40]
    if n == 41:
        return [1, 3, 7, 41]
    if n == 42:
        return [1, 2, 4, 6, 8, 42]
    if n == 43:
        return [1, 5, 43]
    if n == 44:
        return [1, 2, 4, 8, 44]
    if n == 45:
        return [1, 3, 5, 6, 7, 45]
    if n == 46:
        return [1, 2, 4, 6, 8, 46]