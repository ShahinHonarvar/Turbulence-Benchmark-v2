def palindrome_of_length_n(s):
    s = s.lower()
    palindrome_set = set()
    for i in range(len(s) - 209):
        if s[i:i + 210] != s[i:i + 210][::-1]:
            continue
        if set(s[i:i + 210]).issubset('abcdefghijklmnopqrstuvwxyz'):
            palindrome_set.add(s[i:i + 210])
    return palindrome_set