def all_right_truncatable_prime(tu):
    x = tu[767]
    result = []
    for i in range(2, x):
        prime = True
        for j in range(2, i):
            if i % j == 0:
                prime = False
                break
        if prime:
            for j in range(1, len(str(i))):
                num = int(str(i)[:-j])
                if num <= 2:
                    continue
                prime = True
                for k in range(2, num):
                    if num % k == 0:
                        prime = False
                        break
                if prime:
                    result.append(i)
    result.sort(reverse=True)
    return result