def palindromes_of_specific_lengths(txt):
    ans = set()
    for i in range(5):
        for j in range(i - 1, -1, -1):
            t = txt[j:i + 1]
            t = t.lower()
            if t == t[::-1] and 3 <= len(t) <= 4:
                ans.add(t)
    return ans