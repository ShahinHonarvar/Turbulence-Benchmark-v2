def all_left_right_truncatable_prime(tupl):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    x = tupl[177]
    result = []
    for i in range(2, x + 1):
        s = str(i)
        if s.count('0') != 0:
            continue
        remove_left = ''
        remove_right = ''
        while len(s) > 2 and is_prime(int(remove_left + s[1:-1] + remove_right)):
            remove_left += s[0]
            remove_right = s[-1] + remove_right
            s = remove_left + s[1:-1] + remove_right
        if is_prime(int(s)):
            result.append(int(s))
    return sorted(result)