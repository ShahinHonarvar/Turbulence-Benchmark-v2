def palindromes_between_indices(s):
    s = s[6:9]
    result = set()
    for h in range(len(s)):
        for i in range(len(s)):
            if s[h] == s[i]:
                if h == i or h + 1 == i:
                    continue
                for l in range(len(s)):
                    if s[l] == s[h]:
                        if l == h or l == i:
                            continue
                        palindrome1 = s[h] + s[i] + s[l] + s[h]
                        if palindrome1 == palindrome1[::-1]:
                            result.add(palindrome1)
                for l in range(len(s)):
                    if s[l] == s[i]:
                        if l == h or l == i:
                            continue
                        palindrome2 = s[i] + s[h] + s[l] + s[i]
                        if palindrome2 == palindrome2[::-1]:
                            result.add(palindrome2)
    return result