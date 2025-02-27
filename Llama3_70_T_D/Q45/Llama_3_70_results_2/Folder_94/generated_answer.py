def palindromes_between_indices(s):
    s = s[3:5].lower()
    palindromes = set()
    for i in range(3, len(s) + 3):
        for p in __import__('itertools').combinations_with_replacement(s, i):
            palindrome = ''.join(p)
            if palindrome == palindrome[::-1]:
                palindromes.add(palindrome)
    return palindromes