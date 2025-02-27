from collections import defaultdict

def palindrome_of_length_n(s):
    upper = defaultdict(list)
    lower = defaultdict(list)
    for i, ltr in enumerate(s.upper()):
        upper[ltr].append(i)
    for i, ltr in enumerate(s.lower()):
        lower[ltr].append(i)
    ans = set()
    for ltr in lower:
        for i in lower[ltr]:
            if i - 2 >= 0 and s[i - 2:i + 1] in upper:
                for j in upper[s[i - 2:i + 1]]:
                    if j - i + 2 == 3:
                        ans.add(s[j - 2:j + 1])
            if i - 1 >= 0 and i + 1 < len(s) and (s[i - 1:i + 2] in upper):
                for j in upper[s[i - 1:i + 2]]:
                    if j - i + 2 == 3:
                        ans.add(s[j - 2:j + 1])
            if i - 1 >= 0 and i + 2 < len(s) and (s[i - 1:i + 3] in upper):
                for j in upper[s[i - 1:i + 3]]:
                    if j - i + 3 == 3:
                        ans.add(s[j - 3:j + 1])
    return ans