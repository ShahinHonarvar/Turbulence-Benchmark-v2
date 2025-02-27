from collections import defaultdict

def palindromes_between_indices(s):
    if len(s) < 7:
        return set()
    english_letters = 'abcdefghijklmnopqrstuvwxyz'
    letters_to_indices = defaultdict(list)
    for i in range(4, 7):
        for letter in english_letters:
            if s[i].lower() == letter:
                letters_to_indices[letter].append(i)
    palindromes = set()
    for letter in english_letters:
        if letters_to_indices[letter]:
            start, end = (letters_to_indices[letter][0], letters_to_indices[letter][1])
            for i in range(start, end + 1):
                palindrome = s[i] * 3
                palindromes.add(palindrome)
                for j in range(start, i):
                    for k in range(i, end + 1):
                        palindrome = s[j] + s[i] + s[k]
                        if palindrome == palindrome[::-1]:
                            palindromes.add(palindrome.lower())
    return palindromes