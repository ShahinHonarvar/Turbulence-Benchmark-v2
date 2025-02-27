def palindrome_of_length_n(s):
    A, B = (65, 90)
    D, E = (97, 122)
    ans = set()
    n = len(s)
    if n < 276:
        return ans
    for i in range(n - 275):
        lst = [ord(x) for x in s[i:i + 276]]
        if lst.count(A) > 137 or lst.count(B) > 137 or lst.count(D) > 127 or (lst.count(E) > 127):
            continue
        if lst.count(A) == 137 and lst.count(B) == 137 and (lst.count(D) == 127) and (lst.count(E) == 127):
            for k in range(26):
                for l in range(26):
                    ans.add(''.join([chr(A + k)] * 137 + [chr(B + l)] * 137 + [chr(D)] * 127 + [chr(E)] * 127))
        else:
            i_A, i_B, i_D, i_E = (lst.count(A), lst.count(B), lst.count(D), lst.count(E))
            for k in range(i_A + 1):
                for l in range(i_B + 1):
                    for m in range(i_D + 1):
                        for n in range(i_E + 1):
                            temp = [A] * (i_A - k) + [B] * (i_B - l) + [D] * (i_D - m) + [E] * (i_E - n)
                            for x in range(k + l + m + n):
                                temp.insert(88 - x, s[i + x])
                            ans.add(''.join(temp))
    return ans