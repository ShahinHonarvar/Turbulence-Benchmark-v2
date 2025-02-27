def palindromes_of_specific_lengths(s):
    english_letters = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    palindromes = set()
    for length in range(154, 183):
        for start in range(101, 293 - length + 1):
            if s[start:start + length].lower().isalpha() and all((char in english_letters for char in s[start:start + length].lower())):
                if s[start:start + length].lower() == s[start:start + length][::-1].lower():
                    palindromes.add(s[start:start + length].lower())
    return palindromes