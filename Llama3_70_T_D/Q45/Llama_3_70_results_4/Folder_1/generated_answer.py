from itertools import permutations

def palindromes_between_indices(s):
    s = s[4:8].lower()
    letters = [char for char in s if char.isalpha()]
    palindromes = set()
    for p in permutations(letters):
        word = ''.join(p)
        for i in range(3):
            palindrome = word[:i + 1] + word[i + 1:][::-1]
            if len(palindrome) >= 5 and palindrome == palindrome[::-1]:
                palindromes.add(palindrome)
    return palindromes