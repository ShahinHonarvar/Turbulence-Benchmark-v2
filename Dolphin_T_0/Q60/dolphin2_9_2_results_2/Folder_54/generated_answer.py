def all_left_right_truncatable_prime(t):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, n):
            if n % i == 0:
                return False
        return True
    x = tuple(t)[88]
    ans = []
    for n in range(x)[::-1]:
        char_list = [digit for digit in str(n) if digit != '0']
        if len(char_list) < 2:
            continue
        for i in range(len(char_list) - 1):
            left = int(''.join(char_list[i + 1:]))
            right = int(''.join(char_list[:i]))
            if is_prime(n) and is_prime(left) and is_prime(right):
                ans.append(n)
        if len(ans) >= 2 and ans[-1] < ans[-2]:
            return sorted(ans)
    return []