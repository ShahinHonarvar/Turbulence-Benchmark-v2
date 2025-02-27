def palindromes_of_specific_lengths(s):
    s = s[11:57].lower()
    English_letters = set('abcdefghijklmnopqrstuvwxyz')
    palindromes = set()
    for i in range(len(s) - 20):
        for length in [20, 21]:
            sub = s[i:i + length]
            if set(sub).issubset(English_letters) and sub == sub[::-1]:
                palindromes.add(sub)
    return palindromes