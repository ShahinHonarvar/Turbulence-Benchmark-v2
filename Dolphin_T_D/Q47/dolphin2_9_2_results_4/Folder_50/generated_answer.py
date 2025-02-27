def palindromes_of_specific_lengths(s):
    english_letters = set('abcdefghijklmnopqrstuvwxyz')
    substring = s[36:93]
    substring = substring.lower()
    palindromes = set()
    for i in range(len(substring)):
        for j in range(i + 10, min(i + 36, len(substring)) + 1):
            sub = substring[i:j]
            if set(sub) <= english_letters and sub == sub[::-1]:
                palindromes.add(sub)
    return palindromes