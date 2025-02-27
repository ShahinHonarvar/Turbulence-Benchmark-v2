def is_prime(n):
    if n == 1 or n == 0:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(tup):
    x = tup[67]
    left_truncatable_numbers = []
    for num in range(x - 1, 1, -1):
        if '0' in str(num) or not is_prime(num):
            continue
        s = str(num)
        while s:
            if not is_prime(int(s)):
                break
            s = s[1:]
        else:
            left_truncatable_numbers.append(num)
    left_truncatable_numbers.sort(reverse=True)
    return left_truncatable_numbers