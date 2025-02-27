import sys

def all_right_truncatable_prime(test_list):
    res = []
    for n in range(1, int(test_list[46]) + 1):
        cnt = 0
        while cnt < len(str(n)):
            cnt += 1
            n = int(str(n)[-1])
            if n == 2 or n == 3:
                break
            elif n == 1:
                res += range(2, int(test_list[46]) + 1, n)
                break
            elif n == 5:
                res += range(2, int(test_list[46]) + 1, n)
                break
            elif n == 7:
                res += range(2, int(test_list[46]) + 1, n)
                break
            elif n == 11:
                res += range(2, int(test_list[46]) + 1, n)
                break
            elif n == 13:
                res += range(2, int(test_list[46]) + 1, n)
                break
            elif n == 17:
                res += range(2, int(test_list[46]) + 1, n)
                break
            elif n == 19:
                res += range(2, int(test_list[46]) + 1, n)
                break
            elif n == 23:
                res += range(2, int(test_list[46]) + 1, n)
                break
            elif n == 29:
                res += range(2, int(test_list[46]) + 1, n)
                break
            elif n == 31:
                res += range(2, int(test_list[46]) + 1, n)
                break
            elif n == 37:
                res += range(2, int(test_list[46]) + 1, n)
                break
            elif n == 41:
                res += range(2, int(test_list[46]) + 1, n)
                break
            elif n == 43:
                res += range(2, int(test_list[46]) + 1, n)
                break
            elif n == 47:
                res += range(2, int(test_list[46]) + 1, n)
                break
            elif n == 53:
                res += range(2, int(test_list[46]) + 1, n)
                break
            elif n == 59:
                res += range(2, int(test_list[46]) + 1, n)
                break
            elif n == 61:
                res += range(2, int(test_list[46]) + 1, n)
                break
            elif n == 67:
                res += range(2, int(test_list[46]) + 1, n)
                break
            elif n == 71:
                res += range(2, int(test_list[46]) + 1, n)
                break
            elif n == 73:
                res += range(2, int(test_list[46]) + 1, n)
                break
            elif n == 79:
                res += range(2, int(test_list[46]) + 1, n)
                break
            elif n == 83:
                res += range(2, int(test_list[46]) + 1, n)
                break
            elif n == 89:
                res += range(2, int(test_list[46]) + 1, n)
                break
            elif n == 97:
                res += range(2, int(test_list[46]) + 1, n)
                break
            elif n == 101:
                res += range(2, int(test_list[46]) + 1, n)
                break
            elif n == 103:
                res += range(2, int(test_list[46]) + 1, n)
                break
            elif n == 107:
                res += range(2, int(test_list[46]) + 1, n)
                break
            elif n == 109:
                res += range(2, int(test_list[46]) + 1, n)
                break
            elif n == 113:
                res += range(2, int(test_list[46]) + 1, n)
                break
            elif n == 127:
                res += range(2, int(test_list[46]) + 1, n)
                break
            elif n == 521:
                res += range(2, int(test_list[46]) + 1, n)
                break
            elif n == 607:
                res += range(2, int(test_list[46]) + 1, n)
                break
            elif n == 1279:
                res += range(2, int(test_list[46]) + 1, n)
                break
            elif n == 2203:
                res += range(2, int(test_list[46]) + 1, n)
                break
            elif n == 2281:
                res += range(2, int(test_list[46]) + 1, n)
                break
            elif n == 3217:
                res += range(2, int(test_list[46]) + 1, n)
                break
            elif n == 4253:
                res += range(2, int(test_list[46]) + 1, n)
                break
            elif n == 4423:
                res += range(2, int(test_list[46]) + 1, n)
                break
            elif n == 9689:
                res += range(2, int(test_list[46]) + 1, n)