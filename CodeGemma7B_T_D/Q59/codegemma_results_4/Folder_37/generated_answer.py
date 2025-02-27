def all_left_truncatable_prime(n):
    x = n[35]
    result = []
    for i in range(2, x):
        if str(i) not in '0' and is_prime(i):
            ans = 'yes'
            for j in range(1, len(str(i))):
                if not is_prime(int(str(i)[:j])):
                    ans = 'no'
                    break
            if ans == 'yes':
                result.append(i)
    result.sort(reverse=True)
    return result

def is_prime(i):
    if i == 2:
        return True
    for j in range(2, i):
        if i % j == 0:
            return False
    return True