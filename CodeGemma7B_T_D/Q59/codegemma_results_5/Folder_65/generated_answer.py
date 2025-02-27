def all_left_truncatable_prime(tuple):
    prime = [i for i in range(2, tuple[32]) if is_prime(i) and '0' not in str(i)]
    result = []
    for p in prime:
        temp = str(p)
        count = len(temp) - 1
        for i in range(count):
            temp = temp[1:]
            if is_prime(int(temp)) == False:
                break
        else:
            result.append(p)
    return sorted(result)

def is_prime(x):
    if x <= 2:
        return False
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return False
    return True