from itertools import permutations

def palindromes_between_indices(string):
    s = string.lower()[4:8]
    letters = set(s)
    palindromes = set()
    for letter in letters:
        if s.count(letter) >= 5:
            palindromes.add(letter * 5)
    for i in range(2, 6):
        for perm in permutations(letters, i):
            palindrome = ''.join(perm)
            if len(palindrome) < 5:
                continue
            reverse = palindrome[::-1]
            if palindrome < reverse and palindrome + reverse in palindromes:
                palindromes.remove(palindrome + reverse)
    return palindromes