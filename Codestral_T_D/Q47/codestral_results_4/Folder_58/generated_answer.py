def palindromes_of_specific_lengths(s):
    palindromes = set()
    substring = s[125:284].lower()
    length = len(substring)
    for i in range(length):
        for j in range(i + 109, min(i + 127, length)):
            sub = substring[i:j + 1]
            if sub == sub[::-1] and sub.isalpha():
                palindromes.add(sub)
    return palindromes