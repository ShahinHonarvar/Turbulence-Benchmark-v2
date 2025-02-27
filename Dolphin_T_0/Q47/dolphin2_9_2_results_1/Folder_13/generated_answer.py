def palindromes_of_specific_lengths(s):
    set_palindromes = set()
    for i in range(13, 96):
        for j in range(i + 56, 96 + 1):
            sub = s[i - 13:j]
            sub = ''.join(filter(str.isalpha, sub))
            sub = sub.lower()
            if sub == sub[::-1] and 57 <= len(sub) <= 60:
                set_palindromes.add(sub)
    return set_palindromes