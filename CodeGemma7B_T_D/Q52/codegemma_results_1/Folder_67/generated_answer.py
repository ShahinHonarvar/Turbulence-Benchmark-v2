def palindrome_of_length_n(s):
    result = set()
    for i in range(len(s) - 41):
        for j in range(i + 1, len(s) - 40):
            if s[i:j + 1].lower() == s[i:j + 1][::-1].lower():
                result.add(s[i:j + 1])
    return result