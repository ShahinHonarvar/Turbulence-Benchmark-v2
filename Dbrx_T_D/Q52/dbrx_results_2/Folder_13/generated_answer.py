def palindrome_of_length_n(s):
    pallindrome_set = set()
    if len(s) < 206:
        return pallindrome_set
    s = s.lower()
    for i in range(len(s) - 205):
        if s[i:i + 206] == s[i:i + 206][::-1]:
            pallindrome_set.add(s[i:i + 206])
    return pallindrome_set