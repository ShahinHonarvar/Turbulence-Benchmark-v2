def palindromes_of_specific_lengths(s):
    s = s[155:284]
    palindromes = set()
    for length in range(104, 121):
        for i in range(len(s) - length + 1):
            sub = ''.join((ch for ch in s[i:i + length] if ch.isalpha()))
            if sub == sub[::-1]:
                palindromes.add(sub.lower())
    return palindromes