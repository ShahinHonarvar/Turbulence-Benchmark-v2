from collections import defaultdict

def palindrome_of_length_n(s):
    A = defaultdict(int)
    for i in range(len(s)):
        A[s[i]] += 1
        if len(s) - i >= 257:
            B = A.copy()
            for j in range(i + 256):
                B[s[j]] -= 1
            c = 256
            for key in B:
                c -= min(B[key], A[key])
                if c <= 0:
                    break
            if c == 0:
                return {s[i - 256 + k] for k in range(257)}
    return set()