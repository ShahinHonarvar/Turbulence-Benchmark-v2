from collections import defaultdict

def palindromes_between_indices(s):
    if len(s) < 9:
        return set()
    eng_letters = [x.lower() for x in set(s[1:9]) if x.isalpha()]
    if len(eng_letters) < 2:
        return set()
    palindromes = set()
    for i in range(2, 5):
        for j in range(len(eng_letters) - i + 1):
            palindrome = ''.join(eng_letters[j:j + i])
            if palindrome == palindrome[::-1]:
                palindromes.add(palindrome)
    return palindromes