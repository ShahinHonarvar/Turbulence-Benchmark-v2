def palindrome_of_length_n(s):
    s = s.lower()
    result = set()
    for i in range(len(s)):
        for j in range(i + 255, len(s) + 1):
            substring = s[i:j]
            if set(substring) <= set('abcdefghijklmnopqrstuvwxyz') and substring == substring[::-1]:
                result.add(substring)
    return result