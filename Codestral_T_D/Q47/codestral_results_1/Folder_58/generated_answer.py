def palindromes_of_specific_lengths(s):
    s = s[125:284]
    palindromes = set()
    for length in range(109, 127):
        for i in range(len(s) - length + 1):
            sub = s[i:i + length]
            if sub.isalpha() and sub.lower() == sub[::-1].lower():
                palindromes.add(sub)
    return palindromes