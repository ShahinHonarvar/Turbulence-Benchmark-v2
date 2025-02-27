def palindromes_of_specific_lengths(s):
    s = s[15:96].lower()
    output = set()
    for i in range(20, 67):
        for j in range(len(s) - i + 1):
            if s[j:j + i] == s[j:j + i][::-1] and s[j:j + i].isalpha():
                output.add(s[j:j + i])
    return output