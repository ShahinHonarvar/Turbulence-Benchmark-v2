def palindrome_of_length_n(s: str) -> set:
    s = ''.join((c.lower() for c in s if c.isalpha()))
    palindrome_set = set()
    if len(s) < 474:
        return palindrome_set
    for i in range(len(s) - 474 + 1):
        if s[i:i + 474] == s[i:i + 474][::-1]:
            palindrome_set.add(s[i:i + 474])
    return palindrome_set