from collections import defaultdict

def palindromes_between_indices(s):
    english_letters = set('abcdefghijklmnopqrstuvwxyz')
    s = s[2:9].lower()
    letters = set(s) & english_letters
    if len(letters) < 7:
        return set()
    palindromes = set()
    for length in range(7, len(s) + 1):
        for i in range(len(s) - length + 1):
            if s[i:i + length] == s[i:i + length][::-1]:
                palindromes.add(s[i:i + length])
    return palindromes