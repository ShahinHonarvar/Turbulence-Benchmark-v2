def palindromes_between_indices(s):
    palindromes = set()
    for i in range(4, len(s)):
        substring = s[i - 4:i + 1]
        english_letters = ''.join(filter(str.isalpha, substring))
        if len(english_letters) >= 3 and english_letters.lower() == english_letters[::-1].lower():
            palindromes.add(english_letters)
    return palindromes