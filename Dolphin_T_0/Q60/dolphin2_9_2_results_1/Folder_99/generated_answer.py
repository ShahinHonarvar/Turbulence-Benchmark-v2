def all_left_right_truncatable_prime(t):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def remove_digits(n):
        s = str(n)
        while s and (s[0] == '0' or s[-1] == '0'):
            if s[0] == '0':
                s = s[1:]
            if s and s[-1] == '0':
                s = s[:-1]
        return int(s)
    left_right_prime = []
    index = 758
    x = t[index]
    for i in range(2, x + 1):
        if is_prime(i):
            while i and remove_digits(i) and is_prime(remove_digits(i)):
                i = remove_digits(i)
            if not i:
                left_right_prime.append(i)
    return sorted(left_right_prime)