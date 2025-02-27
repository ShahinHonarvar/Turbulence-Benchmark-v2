def palindromes_between_indices(s):
    palindromes = set()
    for i in range(5, min(len(s), 7)):
        substring = s[i - 5:i + 1]
        english_letters = ''.join(filter(str.isalpha, substring)).lower()
        if len(english_letters) >= 3 and english_letters == english_letters[::-1]:
            palindromes.add(english_letters)
    return palindromes