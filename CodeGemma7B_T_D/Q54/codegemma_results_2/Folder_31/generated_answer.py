def right_truncatable_prime():
    x = int(input('Enter a number: '))
    while x > 50:
        x += -1
    for i in range(x):
        factor = 0
        stop = False
        for j in range(2, i + 1):
            if j == i + 1:
                factor = 1
            if i % j == 0:
                factor = j
                stop = True
                break
        if factor == 0 or factor == 1:
            factor = 0
        if factor == 0 and (i >= 5 and len(str(i)) - 1 >= 2):
            tt = i
            while tt >= 10 ** (len(str(i)) - 1):
                if tt % factor == 0:
                    tt = tt // factor
                else:
                    stop = True
                    break
            if stop == False:
                print(i, end=' ')