def is_prime(n):
    if n == 1:
        return False
    else:
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[0]
    result = []
    for i in range(x, 0, -1):
        if '0' in str(i):
            continue
        s = str(i)
        while len(s) > 1 and is_prime(int(s)):
            if len(s) > 2:
                s = s[1:-1]
            else:
                result.append(i)
                break
    return result[::-1]