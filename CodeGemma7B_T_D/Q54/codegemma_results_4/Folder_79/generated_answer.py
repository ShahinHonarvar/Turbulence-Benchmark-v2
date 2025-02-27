def all_right_truncatable_prime(tup):
    x = tup[91]
    right_truncatable_prime = []
    for i in range(2, x):
        for j in range(1, int(i / 2 + 1)):
            k = i % j
            if k == 0:
                break
            if j == int(i / 2):
                for num in range(1, 9):
                    num = str(i)[:len(str(i)) - num]
                    num = int(num)
                    for j in range(1, int(num / 2 + 1)):
                        k = num % j
                        if k == 0:
                            break
                        if j == int(num / 2):
                            right_truncatable_prime.append(i)
    right_truncatable_prime.sort()
    return right_truncatable_prime