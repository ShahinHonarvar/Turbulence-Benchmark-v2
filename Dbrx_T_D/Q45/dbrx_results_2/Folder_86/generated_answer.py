def palindromes_between_indices(s):
    english_letters_lower = set('abcdefghijklmnopqrstuvwxyz')
    english_letters_upper = set('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    english_letters = english_letters_lower | english_letters_upper
    palindromes = set()
    for i in range(6, 10):
        for j in range(i, 10):
            substring = s[i:j + 1]
            letters = set(substring) & english_letters
            if len(letters) >= 4:
                for letter in letters:
                    palindrome = ''.join(sorted(substring.replace(letter, '')) + letter + ''.join(sorted(substring.replace(letter, ''))))
                    palindromes.add(palindrome)
    return palindromes