def all_right_truncatable_prime(n):
    truncatable = []
    for i in range(n - 1, -1, -1):
        num = i
        flag = True
        while num > 0:
            if num % 2 == 0 and num != 2 or (num % 3 == 0 and num != 3) or (num % 5 == 0 and num != 5) or (num % 7 == 0 and num != 7):
                flag = False
                break
            num = int(str(num)[:-1])
        if flag and i % 10 != 0 and (i % 2 != 0) and (i % 5 != 0):
            truncatable.append(i)
    return sorted(truncatable)