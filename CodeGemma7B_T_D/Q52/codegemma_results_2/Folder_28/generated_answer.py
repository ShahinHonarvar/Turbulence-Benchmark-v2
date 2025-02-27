def palindrome_of_length_n(s):
    palindrome_set = set()
    s = s.lower()
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            if s[i:j] == s[i:j][::-1]:
                palindrome_set.add(s[i:j])
    if len(palindrome_set) == 0:
        return set()
    return palindrome_set