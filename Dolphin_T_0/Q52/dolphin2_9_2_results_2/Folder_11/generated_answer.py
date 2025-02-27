def palindrome_of_length_n(s):
    s = s.lower()
    set1 = set()
    for i in range(len(s) - 76):
        if s[i:i + 77] == ''.join(reversed(s[i:i + 77])):
            set1.add(s[i:i + 77])
    return set1