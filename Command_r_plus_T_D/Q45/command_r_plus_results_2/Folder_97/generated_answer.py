def palindromes_between_indices(s):
    s = s.lower()
    english_letters = [char for char in s[0:5] if char.isalpha()]
    palindromes = set()
    for i in range(3, len(english_letters) + 1):
        for j in range(len(english_letters) - i + 1):
            substring = english_letters[j:j + i]
            if substring == substring[::-1]:
                palindromes.add(''.join(substring))
    return palindromes