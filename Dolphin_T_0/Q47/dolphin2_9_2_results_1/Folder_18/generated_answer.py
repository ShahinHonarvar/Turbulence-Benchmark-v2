def palindromes_of_specific_lengths(s):
    s = s[10:84].lower()
    palindromes = set()
    for length in range(13, 67):
        for i in range(0, len(s) - length + 1):
            if s[i:i + length] == s[i:i + length][::-1]:
                word = ''.join(filter(str.isalpha, s[i:i + length]))
                if word == word[::-1]:
                    palindromes.add(word)
    return palindromes