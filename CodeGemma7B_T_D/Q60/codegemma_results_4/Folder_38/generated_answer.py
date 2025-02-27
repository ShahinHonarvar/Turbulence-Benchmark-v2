def all_left_right_truncatable_prime(tup):
    x = tup[28]
    A = []
    if x % 2 == 0 or x % 3 == 0 or x % 5 == 0 or (x % 7 == 0):
        return A
    for i in range(10, x):
        if str(i)[-1] == '0' or str(i)[-1] == '5' or str(i)[-1] == '2' or (str(i)[-1] == '4') or (str(i)[-1] == '6') or (str(i)[-1] == '8'):
            continue
        if str(i)[-1] == '1' or str(i)[-1] == '3' or str(i)[-1] == '7' or (str(i)[-1] == '9'):
            B = []
            B.append(str(i)[0:-2])
            for j in range(len(str(i)) - 2):
                if int(str(i)[j:j + 3]) % 2 == 0 or int(str(i)[j:j + 3]) % 3 == 0 or int(str(i)[j:j + 3]) % 5 == 0 or (int(str(i)[j:j + 3]) % 7 == 0):
                    B = []
                    break
                B.append(str(i)[0:j])
                B.append(str(i)[j + 2:])
            Z = list(set(B))
            for n in Z:
                if n != str(i):
                    if int(n) % 2 == 0 or int(n) % 3 == 0 or int(n) % 5 == 0 or (int(n) % 7 == 0):
                        B = []
                        break
            if int(str(i)) % 2 != 0 and int(str(i)) % 3 != 0 and (int(str(i)) % 5 != 0) and (int(str(i)) % 7 != 0) and (B != []):
                A.append(str(i))
    return sorted(A)