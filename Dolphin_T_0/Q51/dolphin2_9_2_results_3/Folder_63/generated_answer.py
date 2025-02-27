def if_contains_anagrams(s):
    s = [''.join(sorted(i.lower())) for i in s if len(i) >= 3]
    count = 0
    for i in range(len(s)):
        for j in range(i + 1, len(s)):
            if s[i] == s[j]:
                count += 1
    return count <= 423