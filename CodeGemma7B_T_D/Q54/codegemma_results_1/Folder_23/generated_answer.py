def all_right_truncatable_prime(t):
    ans = []
    x = t[77]
    for k in range(2, x):
        if all((str(k)[-i + 1:] in ['2', '3', '5', '7'] for i in range(2, len(str(k)) + 1))):
            truncatable = True
            for i in range(1, len(str(k))):
                if int(str(k)[:-i]) % k != 0:
                    truncatable = False
                    break
            if truncatable:
                ans.append(k)
    ans.sort(reverse=True)
    return ans