def helper_function(num):
    if num < 2:
        return False
    for denominator in range(2, int(num ** 0.5) + 1):
        if num % denominator == 0:
            return False
    return True