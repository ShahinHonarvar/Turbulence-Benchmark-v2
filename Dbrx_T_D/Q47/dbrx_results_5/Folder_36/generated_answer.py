def palindromes_of_specific_lengths(s):
    english_letters = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    s = s[124:284]
    palindromes = set()
    for i in range(124, 284):
        for j in range(115, 135):
            if i + j - 1 >= 284:
                break
            substring = s[i:i + j]
            if len(english_letters & set(substring)) == len(substring):
                if substring == substring[::-1]:
                    palindromes.add(substring.lower())
    return palindromes