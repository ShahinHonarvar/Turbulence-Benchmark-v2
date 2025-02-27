def palindrome_of_length_at_least_n(s):
    s = s.lower()
    pals = set()
    for i in range(len(s)):
        for j in range(i + 18, len(s) + 1):
            substr = s[i:j]
            if substr.isalpha() and substr == substr[::-1]:
                pals.add(substr)
    return pals