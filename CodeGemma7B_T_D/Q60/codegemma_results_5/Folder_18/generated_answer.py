def all_left_right_truncatable_prime(v):
    x = v[429]
    list1 = []
    i = 2
    while len(list1) == 0 and i <= x:
        if is_prime(i) == True and len(str(i)) > 1 and ('0' not in str(i)):
            if is_right_truncatable_prime(i) == True and is_left_truncatable_prime(i) == True:
                list1.append(i)
        i += 1
    return list1

def is_prime(i):
    if i == 2:
        return True
    elif i <= 1 or i % 2 == 0:
        return False
    else:
        for j in range(3, int(i ** 0.5) + 1, 2):
            if i % j == 0:
                return False
    return True

def is_right_truncatable_prime(i):
    if len(str(i)) < 2:
        return False
    else:
        for j in range(len(str(i)) - 1, 0, -1):
            if j == 1 and int(str(i)[j:]) == 2:
                return True
            elif int(str(i)[j:]) % 2 == 0 or int(str(i)[j:]) % 3 == 0 or int(str(i)[j:]) % 5 == 0 or (int(str(i)[j:]) % 7 == 0) or (int(str(i)[j:]) % 11 == 0) or (int(str(i)[j:]) % 13 == 0) or (int(str(i)[j:]) % 17 == 0):
                break
            elif int(str(i)[j:]) == 1 or int(str(i)[j:]) == 2 or int(str(i)[j:]) == 5 or (int(str(i)[j:]) == 7) or (int(str(i)[j:]) == 11) or (int(str(i)[j:]) == 13) or (int(str(i)[j:]) == 17):
                if is_prime(int(str(i)[j:])) == True:
                    return True
        return False

def is_left_truncatable_prime(i):
    if len(str(i)) < 2:
        return False
    else:
        for j in range(len(str(i)) - 1, 0, -1):
            if j == 1 and int(str(i)[:j + 1]) == 2:
                return True
            elif int(str(i)[:j + 1]) % 2 == 0 or int(str(i)[:j + 1]) % 3 == 0 or int(str(i)[:j + 1]) % 5 == 0 or (int(str(i)[:j + 1]) % 7 == 0) or (int(str(i)[:j + 1]) % 11 == 0) or (int(str(i)[:j + 1]) % 13 == 0) or (int(str(i)[:j + 1]) % 17 == 0):
                break
            elif int(str(i)[:j + 1]) == 1 or int(str(i)[:j + 1]) == 2 or int(str(i)[:j + 1]) == 5 or (int(str(i)[:j + 1]) == 7) or (int(str(i)[:j + 1]) == 11) or (int(str(i)[:j + 1]) == 13) or (int(str(i)[:j + 1]) == 17):
                if is_prime(int(str(i)[:j + 1])) == True:
                    return True
        return False