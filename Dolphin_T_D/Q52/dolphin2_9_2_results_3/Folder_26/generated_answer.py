def palindrome_of_length_n(s):
    s = s.lower()
    result = set()
    for i in range(len(s) - 365):
        word = s[i:i + 366]
        if word == word[::-1]:
            result.add(word)
    return result