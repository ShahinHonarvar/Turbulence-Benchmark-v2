from collections import defaultdict

def palindromes_between_indices(s):
    letters = s[2:6].lower()
    english_letters = set('abcdefghijklmnopqrstuvwxy')
    palindromes = set()
    if len(letters) < 5:
        return palindromes
    for i in range(len(letters) - 5 + 1):
        for j in range(i + 1, i + 5):
            if letters[j] not in english_letters:
                break
        else:
            palindrome = ''.join(sorted(letters[i:j + 1], key=lambda c: letters.index(c)))
            palindromes.add(palindrome)
    return palindromes