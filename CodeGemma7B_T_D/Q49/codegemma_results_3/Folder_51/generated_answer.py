def if_decimal_is_divisible(binary):
    fib = [0, 1]

    def getPrime(num):
        factor = 2
        while factor * factor <= num:
            if num % factor == 0:
                return factor
            factor += 1
        return None
    flag = False
    for i in range(2, len(binary) + 1):
        decimal = int(binary[0:i], 2)
        while decimal not in fib:
            fib.append(fib[-1] + fib[-2])
        if getPrime(fib.index(decimal)) == 17:
            flag = True
            break
    return flag