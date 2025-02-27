def palindromes_of_specific_lengths(s):
    s = s[154:284]
    palindromes = set()
    for i in range(104, 121):
        for j in range(0, len(s) - i + 1):
            if s[j:j + i].lower() == s[j:j + i][::-1].lower() and s[j:j + i].isalpha():
                palindromes.add(s[j:j + i])
    return palindromes