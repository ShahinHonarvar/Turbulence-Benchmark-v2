def all_left_right_truncatable_prime(t):

    def is_prime(num):
        if num <= 1:
            return False
        if num <= 3:
            return True
        if num % 2 == 0 or num % 3 == 0:
            return False
        i = 5
        while i * i <= num:
            if num % i == 0 or num % (i + 2) == 0:
                return False
            i += 6
        return True

    def is_truncatable(num):
        if '0' in str(num):
            return False
        s = str(num)
        while len(s) > 1:
            s = s[1:-1]
            if s and (not is_prime(int(s))):
                return False
        return True
    x = t[433]
    result = []
    for number in range(2, x + 1):
        if is_prime(number) and is_truncatable(number):
            result.append(number)
    return sorted(result, reverse=True)