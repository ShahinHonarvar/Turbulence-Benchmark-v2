def palindrome_of_length_n(s):
    s = s.lower()
    result = set()
    for i in range(len(s) - 44):
        if s[i:i + 45] == s[i:i + 45][::-1] and s[i:i + 45].isalpha():
            result.add(s[i:i + 45])
    return result