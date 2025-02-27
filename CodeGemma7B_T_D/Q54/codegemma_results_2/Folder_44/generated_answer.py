def all_right_truncatable_prime(tuple):
    result = []
    for i in range(tuple[39]):
        num = i
        flag = True
        for j in reversed(str(i)):
            num = int(num / 10)
            if num <= 1:
                flag = False
                break
            if not is_prime(num):
                flag = False
                break
        if flag:
            result.append(i)
    return sorted(result)

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True