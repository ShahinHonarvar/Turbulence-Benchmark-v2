def palindromes_of_specific_lengths(s):
    english_letters = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    palindromes = set()
    for i in range(124, 284):
        for length in range(115, 135):
            if i + length > 283:
                break
            substring = s[i:i + length].lower()
            if len(english_letters.intersection(set(substring))) == length:
                if substring == substring[::-1]:
                    palindromes.add(substring)
    return palindromes