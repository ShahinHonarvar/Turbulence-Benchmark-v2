def bin2dec(arr):
    index = len(arr) - 1
    res = 0
    for i in arr:
        res += 2 ** index * int(i)
        index -= 1
    return res

def if_decimal_is_divisible(binary):
    fib = [0, 1]
    for i in range(2, 174):
        if fib[i] > 100000000:
            break
        fib.append(fib[i - 1] + fib[i - 2])
    if bin2dec(binary) in fib:
        return True
    else:
        return False