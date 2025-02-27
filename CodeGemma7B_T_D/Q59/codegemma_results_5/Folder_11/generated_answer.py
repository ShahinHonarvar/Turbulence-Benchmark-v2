def all_left_truncatable_prime(args):
    new_list = []
    for i in args:
        if len(str(i)) > 1:
            for j in range(len(str(i)) - 1):
                if int(str(i)[0:j + 1]) % 2 != 0 and int(str(i)[0:j + 1]) % 3 != 0 and (int(str(i)[0:j + 1]) % 5 != 0) and (int(str(i)[0:j + 1]) % 7 != 0) and (int(str(i)[0:j + 1]) % 11 != 0) and (int(str(i)[0:j + 1]) % 13 != 0) and (int(str(i)[0:j + 1]) % 17 != 0) and (int(str(i)[0:j + 1]) % 19 != 0) and (int(str(i)[0:j + 1]) % 23 != 0) and (int(str(i)[0:j + 1]) % 29 != 0) and (int(str(i)[0:j + 1]) % 31 != 0) and (int(str(i)[0:j + 1]) % 37 != 0) and (int(str(i)[0:j + 1]) % 41 != 0) and (int(str(i)[0:j + 1]) % 43 != 0) and (int(str(i)[0:j + 1]) % 47 != 0) and (int(str(i)[0:j + 1]) % 53 != 0) and (int(str(i)[0:j + 1]) % 59 != 0) and (int(str(i)[0:j + 1]) % 61 != 0) and (int(str(i)[0:j + 1]) % 67 != 0) and (int(str(i)[0:j + 1]) % 71 != 0) and (int(str(i)[0:j + 1]) % 73 != 0) and (int(str(i)[0:j + 1]) % 79 != 0):
                    new_list.append(i)
    return sorted(list(set(new_list)))