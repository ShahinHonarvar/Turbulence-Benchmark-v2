from collections import defaultdict

def palindromes_between_indices(s):
    letters = [set(filter(str.isalpha, c.lower())) for c in s[3:7]]
    palindromes = set()
    for i in range(len(letters)):
        for j in range(i, len(letters)):
            palindrome = ''.join(letters[i:j + 1] + list(reversed(letters[i:j + 1])))
            if len(palindrome) >= 3 and palindrome == palindrome[::-1]:
                palindromes.add(palindrome)
    return palindromes