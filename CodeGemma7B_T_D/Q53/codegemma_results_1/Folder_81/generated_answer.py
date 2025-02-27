def palindrome_of_length_at_least_n(s: str) -> set:
    ans = set()
    for i in range(len(s)):
        for j in range(i, len(s)):
            t = s[i:j + 1]
            if t == t[::-1] and len(t) >= 33 and (t.lower() == t):
                ans.add(t)
    return ans