def palindrome_of_length_at_least_n(s):
    s = s.lower()
    result = set()
    for i in range(len(s)):
        for j in range(i + 13, len(s) + 1):
            if s[i:j].strip() and set(s[i:j].strip()) <= set('abcdefghijklmnopqrstuvwxyz') and (s[i:j].strip() == s[i:j].strip()[::-1]):
                result.add(s[i:j].strip())
    return result