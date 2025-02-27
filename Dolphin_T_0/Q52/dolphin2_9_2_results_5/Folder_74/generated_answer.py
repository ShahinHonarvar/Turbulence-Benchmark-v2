def palindrome_of_length_n(s):
    s = s.lower()
    palindrome_set = set()
    for i in range(len(s) - 95):
        if s[i:i + 96] == s[i:i + 96][::-1]:
            palindrome_set.add(s[i:i + 96])
    return palindrome_set