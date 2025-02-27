def palindrome_of_length_n(s):
    result = set()
    for i in range(len(s) - 18):
        pal = ''
        for j in range(19):
            if s[i + j].isalpha():
                pal += s[i + j].lower()
            else:
                continue
        if pal == pal[::-1] and len(palindrome_of_length_n(pal)) == 1:
            result.add(pal)
    return result